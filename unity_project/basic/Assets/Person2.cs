using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using System;

public class Person2 : MonoBehaviour
{
    // Start is called before the first frame update
    void Awake() {
        
    }
    
    void Start()
    {
        System.Diagnostics.Stopwatch sw = new System.Diagnostics.Stopwatch();
        sw.Start();

        List<int> l1 = new List<int>();
        for (int i = 0; i<0x3ffFfff; i++ )
        {
            l1.Add(i);
        }
        int i1 = l1[0x3ffFfff - 1];
        l1.Remove(0x3ffFfff - 1);

        sw.Stop();
        Debug.Log("ElapseMeilliseconds :" + sw.ElapsedMilliseconds.ToString() + "ms");
        
        // transform.Translate(1,1,1);
        GameObject PrefabGameObject = (GameObject)Resources.Load("Prefabs/Capsule");
        GameObject obj = Instantiate(PrefabGameObject);

        obj.transform.Translate(3,3,3);
        // Destroy(obj);
    }

    // Update is called once per frame
    public float mX = 0;
    public float mY = 0;
    public float mZ = 0;

    void Update()
    {
       

        // TextP1.gText = transform.position.ToString();
        TextP1.gText2 = transform.position.ToString();
        if(mZ < 4.5f){
            mZ += Time.deltaTime * 0.9f;
            transform.position = new Vector3(-0.73f, -8.32f, 2.38f + mZ);
            //Debug.Log("pos_Z :" + transform.position.z);
            // position_Z = transform.position   
        }
        else {
            if (mX < 2.5f){
                mX += Time.deltaTime * 1.2f;
                transform.position = new Vector3(-0.73f - mX, -8.32f, 2.38f + mZ);
            }
            else{
                if (mZ < 10.0f){
                    mZ += Time.deltaTime * 1.2f;
                    transform.position = new Vector3(-0.73f - mX, -8.32f, 2.38f + mZ);
                }
                else {
                    if(mX < 4.0f){
                        mX += Time.deltaTime * 0.9f;
                        transform.position = new Vector3(-0.73f - mX, -8.32f, 2.38f + mZ);
                        TextP1.gText2_1 = transform.position.ToString();
                    }
                }
            }
        }
        // transform.Translate(0.01f, 0, 0);

        //Debug.Log("Updata yyy");
        //Debug.Log("Update:" + Time.deltaTime);
        


    }
}
