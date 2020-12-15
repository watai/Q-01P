using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class MainManager : MonoBehaviour
{
    [SerializeField] WebSocketManager WebSocket;

    void Start()
    {
        WebSocket.Setup();
    }

    // Update is called once per frame
    void Update()
    {
        
    }
}
