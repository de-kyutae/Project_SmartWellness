using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class ChatiptScrt : MonoBehaviour
{
    public GameObject mOBJ;
    public void chatiptComplete(string s1)
    {
        using (JcCtUnity1.PkWriter1Nm pkw = new JcCtUnity1.PkWriter1Nm(1))
        {
            pkw.wStr1(s1);
            Client.gThis.send(pkw);
        }
        GetComponent<UnityEngine.UI.InputField>().text = "";
    }
    

    // Start is called before the first frame update
    void Start()
    {
        
    }

    // Update is called once per frame
    void Update()
    {
        
    }
    
    void OnMouseDown()
    {


        Debug.Log("OnMouseDown");
        Vector3 v3 = transform.position;
        v3.y += 1;
        using (JcCtUnity1.PkWriter1Nm pkw = new JcCtUnity1.PkWriter1Nm(2))
        {
            pkw.wReal32(v3.x);
            pkw.wReal32(v3.y);
            pkw.wReal32(v3.z);
            Client.gThis.send(pkw);
        }
        Client.gThis.mObj = gameObject;

    }


}
