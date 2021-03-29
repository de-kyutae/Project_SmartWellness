using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class TextP1 : MonoBehaviour
{
    static public string gText1 = "empty";
    static public string gText1_1 = "empty";
    static public string gText2 = "empty";
    static public string gText2_1 = "empty";
    public TextMesh mTm;
    //public GameObject target_person1;
    
    // Start is called before the first frame update
    void Start()
    {
        // target_person1 = GameObject.Find("p1");
    }

    // Update is called once per frame
    void Update()
    {
        if (gText1 == gText1_1 && gText2 == gText2_1){
            mTm = GetComponent<TextMesh>();
            mTm.text = "완료";
        }
        else {
            mTm = GetComponent<TextMesh>();
            mTm.text = "처리중";
        }
        // // Vector3 spotPerson1=target_person1.transform.position;
        // mTm = GetComponent<TextMesh>();
        // mTm.text = TextP1.gText;
        // // mTm.text = spotPerson1.ToString();
    }
}
