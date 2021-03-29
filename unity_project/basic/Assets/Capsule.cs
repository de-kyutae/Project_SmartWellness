using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Capsule : MonoBehaviour
{
    public float x_point;
    //public List<Capsule> Capsule_list;
   
    // Start is called before the first frame update
    void Start()
    {
        //List<GameObject> student_list = Bus.Position_list;
        //List<GameObject> text_list = Bus.Text_list;
    }

    // Update is called once per frame
    void Update()
    {
        //List<GameObject> student_list = Bus.Position_list;
        //List<GameObject> text_list = Bus.Text_list;
    }
    void OnMouseDown()
    {
        int student_count = Bus.Position_list.Count;
        int student_index = Bus.Position_list.IndexOf(gameObject);

        int text_count = Bus.Text_list.Count;

        //GameObject go = Bus.Position_list[index];
        // GameObject go = Bus.Position_list[1];
        Debug.Log("index :" + student_index + " student count" + student_count);
        Destroy(Bus.Text_list[student_index]);
        Bus.Position_list.RemoveAt(student_index);
        Bus.Text_list.RemoveAt(student_index);

        student_count = Bus.Position_list.Count;


        for (int i = student_index; i < student_count; i++)
        {
            Bus.Position_list[i].transform.Translate(1.0f, 0.0f, 0.0f);
            Bus.Text_list[i].transform.Translate(1.0f, 0.0f, 0.0f);
        }

        Destroy(gameObject);
        

       /* Vector3 check_position;
        check_position = transform.position;
        Debug.Log(Capsule_list[1]);*/
        //Debug.Log(check_position);
        //int key_index = Capsule_list.IndexOf(check_position);
        //Debug.Log(key_index);
    }
    void OnMouseUp()
    {

    }
}