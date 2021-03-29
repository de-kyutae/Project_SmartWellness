using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Ca
{
    static public Ca gThis = new Ca();
    public float mX = -123;
    public string mTxt = "Ca.txt";
}


public class p1 : MonoBehaviour
{
    
    public Material mMaterial;
    public Ca mA = new Ca();
    // public Ca2 mA2; // = new Ca2();
    public Vector3 mPosition;

    void Awake(){
        Ca.gThis.mTxt = "gThis";
        Debug.Log("Awake p1, Ca:" + mA.mTxt);
        // Debug.Log("Awake p2, Ca:" + Ca.gYthis.mTxt);
    }
    
    // Start is called before the first frame update
    void Start()
    {
        transform.Translate(0, 0, 0);
        mPosition = new Vector3(-0.73f, -8.32f, 2.38f);
        Debug.Log("Start");
        mMaterial = GetComponent<Renderer>().material;
    }

    // public float x = 0;
    // public float y = 0;
    // public float z = 0;
    // public float mX1 = 0;
    // public static transform.position
    // Update is called once per frame
    void Update()
    {
        TextP1.gText1 = transform.position.ToString();
        if(mPosition.z < 7.0f){
            mPosition.z += Time.deltaTime * 1.2f;
            transform.position = mPosition;
            //Debug.Log("pos_Z :" + transform.position.z);
            // position_Z = transform.position   
        }
        else {
            if (mPosition.x > -3.2f){
                mPosition.x -= Time.deltaTime * 1.2f;
                // transform.position = new Vector3(-0.73f - mX, -8.32f, 2.38f + mZ);
                transform.position = mPosition;
            }
            else{
                if (mPosition.z < 17.0f){
                    mPosition.z += Time.deltaTime * 1.2f;
                    // transform.position = new Vector3(-0.73f - mX, -8.32f, 2.38f + mZ);
                    // mX1 = transform.position.x;
                    // Debug.Log("pos_X :" + mX1);
                    transform.position = mPosition;

                }
                else {
                    if (mPosition.x < 1.0f)
                    {
                        mPosition.x += Time.deltaTime * 0.9f;
                        transform.position = mPosition;
                        // transform.position = new Vector3(mX1 + mX, -8.32f, 2.38f + mZ);
                        //Debug.Log("pos_X :" + transform.position.x);
                        TextP1.gText1_1 = transform.position.ToString();
                    }
                }
            }
        }         

        // transform.Translate(0.01f, 0, 0);
        
        //Debug.Log("Updata yyy");
        //Debug.Log("Update:" + Time.deltaTime);
    }
    void OnMouseDown() 
    {
        Debug.Log("OnMouseDown");
        mMaterial.color = Color.red;
    }
    void OnMouseUp() 
    {
        Debug.Log("OnMouseUp");
    }
    void OnDestroy(){
        Destroy(mMaterial);
    }
}

