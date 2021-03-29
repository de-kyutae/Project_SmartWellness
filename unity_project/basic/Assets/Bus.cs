using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Bus : MonoBehaviour
{

    public float mX = 0;
    static public int count = 1;
    static public List<GameObject> Position_list = new List<GameObject>(); // Capsule 리스트용
    static public List<GameObject> Text_list = new List<GameObject>();
    public GameObject obj;


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
        int count = Bus.Position_list.Count; 
        GameObject PrefabGameObject = (GameObject)Resources.Load("Prefabs/Capsule");
        GameObject obj = Instantiate(PrefabGameObject);
        obj.transform.position = this.transform.position; 
        obj.transform.Translate(-2 - count, 0.0f, 0.0f);
        Bus.Position_list.Add(obj);


        // Debug.Log(Position_list[0]);
        //Bus.Position_list.IndexOf(obj);

        GameObject TextGameObject = (GameObject)Resources.Load("Prefabs/Nstudent");
        GameObject mText = Instantiate(TextGameObject);
        mText.transform.position = this.transform.position;
        mText.transform.Translate(-2.5f -count, 1.0f, 1.0f);
        Bus.Text_list.Add(mText);

    }
    void OnMouseUp()
    {
        if (count < 10)
        {
            mX += 1.0f;
            count += 1;
        }
        
        Debug.Log("OnMouseUp");
    }
    void OnDestroy()
    {

    }

}
//Capsule.cs
//Capsule1 s1 = this;
//GameObject go = s1.gameObject;
//Script1 s2 = go.GetComponent<scropt1>();
