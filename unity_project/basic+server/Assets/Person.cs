using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Person : MonoBehaviour
{
    public bool clicked;
    List<bool> selected_person_list = new List<bool>();
    TextMesh mTm;
    Vector3 position;
    // Start is called before the first frame update
    void Start()
    {
        mTm = GetComponentInChildren<TextMesh>();
        mTm.text = "ÇÐ»ý" + Bus.person_count;

        GetComponentInChildren<GameObject>();

    }

    // Update is called once per frame
    void Update()
    {
   
    }
    void OnMouseDown()
    {

        int person_number = Bus.Person_List.Count;
        int person_index = Bus.Person_List.IndexOf(gameObject);
        


        
        
        //Bus.Person_List[person_index] = true;
        
        for (int i = person_index; i<person_number; i++)
        {
            if (i != person_index)
            {

            }
        }
        Vector3 location = gameObject.transform.position;
        transform.Translate(0.0f,0.0f,0.5f);
        Debug.Log(location);
    }
}
