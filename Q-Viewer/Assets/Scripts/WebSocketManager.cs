using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using WebSocketSharp;
using WebSocketSharp.Net;

// https://github.com/sta/websocket-sharp#websocket-client

public class WebSocketManager : MonoBehaviour
{
    private float count;
    private WebSocket ws;
    private List<string> MessageList = new List<string>();

    void Update()
    {
        count += Time.deltaTime;
        if (count >= 3.0f) {
            WebSocketState state = ws.ReadyState;
            bool isAlive = ws.IsAlive;
            if (state == WebSocketState.Closed && !isAlive) {
                // string msg = "WebSocket:Reopen";
                // Debug.Log(msg);
                // LogManager.Instance.Write(msg);
                // ws.Connect();
            }
            count = 0.0f;
        }
    }

    public void Setup()
    {
       if (ws == null) Connect();
    }

    public void Close()
    {
        ws.Close();
        ws = null;
        // remove list
        MessageList.Clear();
        Debug.Log("Clear Message List");
    }

    private void Connect()
    {   
        string url = GetURL();

        ws = new WebSocket(url);
        string msg = $"WebSocket:Connect to {url}";
        Debug.Log(msg);
        LogManager.Instance.Write(msg);

        ws.OnOpen += (sender, e) =>
        {
            msg = "WebSocket:Open";
            Debug.Log(msg);
            LogManager.Instance.Write(msg);
        };

        ws.EmitOnPing = true;
        ws.OnMessage += (sender, e) =>
        {
            string data = "";
            if (e.IsPing) {
                data = "Received a ping.";
            } else {
                data = e.Data;
                MessageList.Add(data);
            }
            Debug.Log("WebSocket Message: " + data);
        };

        ws.OnError += (sender, e) =>
        {
            Debug.Log("WebSocket Error Message: " + e.Message);
        };

        ws.OnClose += (sender, e) =>
        {
            msg = "WebSocket:Close";
            Debug.Log(msg);
        };

        ws.Connect();
    }

    private void OnDestroy()
    {
        Close();
    }

    private string GetPort()
    {
        string port = "9001";
        return port;
    }

    private string GetURL()
    {
        string port = GetPort();
        // string url = "ws://192.168.11.128:" + port;
        string url = "ws://q-01p.local:" + port;
        return url;
    }

    public string GetLastMessage(bool isRemoved)
    {
        string msg;
        if (MessageList.Count > 0) {
            msg = MessageList[0];
            if (isRemoved) MessageList.RemoveAt(0);
        } else {
            msg = "";
        }
        return msg;
    }

    public void SendStatusMessage(string msg)
    {
        string json;
        json = JsonFormatter("status", "status", msg);
        ws.Send(json);
    }

    public void SendCommandMessage(string name, string msg)
    {
        string json;
        json = JsonFormatter("cmd", name, msg);
        ws.Send(json);
    }

    // For Post Request
    public void SendUserId(string userId)
    {
        string json = JsonFormatter("status", "result", userId);
        ws.Send(json);
    }

    public void OnSendUserId(string result)
    {
        SendUserId(result);
    }

    public void SendErrorMessage(string msg)
    {
        string json = JsonFormatter("status", "status", "error-upload");
        ws.Send(json);
    }

    public void OnSendErrorMessage(string msg)
    {
        SendErrorMessage(msg);
    }

    private string JsonFormatter(string type, string name, string message)
    {
        JsonData data = new JsonData();
        data.type = type;
        data.name = name;
        data.message = message;
        return JsonUtility.ToJson(data);
    }
}