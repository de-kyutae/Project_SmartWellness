using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Name : MonoBehaviour
{
    public TextMesh mTm;

    // Start is called before the first frame update
    void Start()
    {
        mTm = GetComponent<TextMesh>();
        mTm.text = "ÇÐ»ý" + Bus.person_count;
        Debug.Log("Person count:" + Bus.person_count);
    }

    // Update is called once per frame
    void Update()
    {
        
    }
}
