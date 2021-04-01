using System.Collections;
using System.Collections.Generic;
using UnityEngine;

class Client : JcCtUnity1.JcCtUnity1
{
	static public Client gThis = new Client();

	public Client() : base(System.Text.Encoding.Unicode) { }

    public GameObject mObj { get; internal set; }

    public void qv(string s1) { innLogOutput(s1); }

	// JcCtUnity1.JcCtUnity1
	protected override void innLogOutput(string s1) { Debug.Log(s1); }
	protected override void onConnect(JcCtUnity1.NwRst1 rst1, System.Exception ex = null)
	{
		qv("Dbg on connect: " + rst1);
		//int pkt = 1111;
		//using (JcCtUnity1.PkWriter1Nm pkw = new JcCtUnity1.PkWriter1Nm(pkt))
		//{
		//	pkw.wInt32u(2222);
		//	this.send(pkw);
		//}
		//qv("Dbg send packet Type:" + pkt);

	}
	protected override void onDisconnect()
	{ qv("Dbg on disconnect"); }

	
    protected override bool onRecvTake(Jc1Dn2_0.PkReader1 pkrd)
	{ 
		//qv("Dbg on recv: " + pkrd.getPkt()/* + pkrd.ReadString()*/ );  
		switch (pkrd.getPkt())
        {
			case 1:
				string txt = pkrd.rStr1def();
				Debug.Log("Pkrv:" + txt);
				break;
			case 2:
				if (mObj)
                {
					mObj.transform.position = new Vector3(pkrd.rReal32(), pkrd.rReal32(), pkrd.rReal32());
				}
				break;
                
        }
		return true;
	}
}
public class Clientgo : MonoBehaviour
{
    // Start is called before the first frame update
    void Start()
    {
		Client.gThis.connect("127.0.0.1", 7777);

	}

    // Update is called once per frame
    void Update()
    {
		Client.gThis.framemove();
    }

}


