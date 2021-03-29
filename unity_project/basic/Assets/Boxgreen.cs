using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Boxgreen : MonoBehaviour
{
    // Start is called before the first frame update
    void Start()
    {
        
    }

    // Update is called once per frame
    void Update()
    {
        //transform.Rotate(new Vector3(0, 50, 0));
    }
    private void OnMouseDrag()
    {
        transform.rotation = Quaternion.Euler(0, 100, 0);
    }
}

//TextMesh tm = GetComponentInChildren<TextMesh>;
//tm.text = "aaa";