using System.Collections;
using System.Collections.Generic;
using System.IO;
using System;
using UnityEngine;

public class LogManager : Singleton<LogManager>
{
    [SerializeField] bool IsEnabled;
    private string filePath;

    protected override void Awake()
	{
		if (this != Instance) {
			Destroy(this);
			return;
		}
        Initialize();
		// DontDestroyOnLoad(this.gameObject);
    }

    private void Initialize()
    {
        if (IsEnabled) {
            string datetime = DateTime.Now.ToString("yyyyMMddHHmmss");
            if (Application.platform == RuntimePlatform.IPhonePlayer) {
                filePath = Application.persistentDataPath + "/log_" + datetime + ".txt";
            }　else  {
                filePath = Application.dataPath + "/Result/log_" + datetime + ".txt";
            }
            Debug.Log($"Log file path: {filePath}");
        } 
    }

    public void Write(string msg)
    {
        if (this != null && IsEnabled) {
            try {
                using (var writer = new StreamWriter(filePath, true))
                {
                    string datetime = DateTime.Now.ToString("yyyy/MM/dd HH:mm:ss");
                    string log = datetime + "\t\t" + msg;
                    writer.WriteLine(log);
                    writer.Flush();
                    writer.Close();
                }
            } 
            catch (Exception e) {
                Debug.Log(e.Message);
            }
        }        
    }
}
