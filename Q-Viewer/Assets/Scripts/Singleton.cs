using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Singleton<T> : MonoBehaviour where T : MonoBehaviour
{
    private static T mInstance;
    public static T Instance
    {
        get {
            if (mInstance == null) {
                mInstance = (T)FindObjectOfType(typeof(T));
                if (mInstance == null) {
                    Debug.LogError (typeof(T) + "is nothing");
                }
            }
    
            return mInstance;
        }
    }

    virtual protected void Awake()
    {
        CheckInstance();
    }

    protected bool CheckInstance()
    {
        if (mInstance == null) {
            mInstance = this as T;
            return true;
        } else if (Instance == this) {
            return true;
        }
        Destroy (this);
        return false;
    }
}