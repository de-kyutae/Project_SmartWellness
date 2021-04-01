using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Bus : MonoBehaviour
{
    public float mX = 0;
    static public int person_count = 0;
    GameObject Person;
    static public List<GameObject> Person_List = new List<GameObject>();
    
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
        if (Bus.person_count <10)
        {
            int modified_count = Bus.Person_List.Count;
            GameObject PrefabGameObjectPerson = (GameObject)Resources.Load("Prefabs/Person");
            GameObject Person = Instantiate(PrefabGameObjectPerson);
            Person.transform.position = this.transform.position;
            Person.transform.Translate(-1.0f - modified_count * 0.4f, 0.0f, -1.0f);
            Bus.Person_List.Add(Person);

            mX += 1.0f;
            person_count += 1;
            //Debug.Log(person_count);



        }
        

    }
    void OnMouseUp()
    {
/*        if (Bus.person_count < 10)
        {
            mX += 1.0f;
            person_count += 1;
            Debug.Log(person_count);
        }
        else
        {
            Destroy(Person);
        }*/
    }
    void OnDestory()
    {

    }
}
