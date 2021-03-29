using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Nstudent : MonoBehaviour
{
    public TextMesh mTm;

    // Start is called before the first frame update
    void Start()
    {
        mTm = GetComponent<TextMesh>();
        mTm.text = "ÇÐ»ý" + Bus.count;
    }

    // Update is called once per frame
    void Update()
    {
        
    }
}
