
int Eile[16]={13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, A5, A4};
///// Lemputes: 1   2   3   4  5  6  7  8  9  10 11 12 13 14 15 16
int Aukstas[4]={ A0, A1, A2, A3};
/////// Aukstai:  1   2   3   4  

//////////MIRKSEJIMO GREICIAI///////////
int labailetas = 500;                  //
int letas = 300;                       //
int vidutinis = 200;                   //
int greitas = 100;                     //
int labaigreitas = 50;                 //
int zaibiskas = 3;                     //
////////////////////////////////////////
void setup()
{
  for (int i = 0; i < 16; i++)
  pinMode (Eile[i], OUTPUT);
  for (int i = 0; i < 4; i++)
  pinMode (Aukstas[i], OUTPUT);

}

void loop() // besikartojanti procedura.
{
  VisosIjungtos();
  delay(500);
  VisosIsjungtos();
  MirksiRaudonos();
  MirksiGeltonos();
  for (int i = 0; i < 4; i++){
    
    for (int i = 0; i < 20; i++)
     IjungtosRaudonos();
    for (int i = 0; i < 20; i++)
      IjungtosGeltonos();
  }
  Test();
}

void VisosIjungtos() // Ijungiamos visos lemputes.
{
  VisosIsjungtos();
  for (int i = 0; i < 16; i++)
  digitalWrite(Eile[i], 1);
  for (int i = 0; i < 4;  i++)
  digitalWrite(Aukstas[i], 0);
}
void VisosIsjungtos() // Isjungiamos visos lemputes.
{
  for (int i = 0; i < 16; i++)
  digitalWrite(Eile[i], 0);
  for (int i = 0; i < 4;  i++)
  digitalWrite(Aukstas[i], 1);
}
//********************************************************************************************//
void MirksiRaudonos() // Mirksi TIK raudonos lemputes.
{
  VisosIsjungtos();
  digitalWrite(Eile[0], 1);
  digitalWrite(Eile[2], 1);
  digitalWrite(Eile[5], 1);
  digitalWrite(Eile[7], 1);
  digitalWrite(Eile[8], 1);
  digitalWrite(Eile[10], 1);
  digitalWrite(Eile[13], 1);
  digitalWrite(Eile[15], 1);
  digitalWrite(Aukstas[3],0);
  delay(vidutinis);
VisosIsjungtos();
 ///////////////////////////////////////////
  digitalWrite(Eile[1], 1);
  digitalWrite(Eile[3], 1);
  digitalWrite(Eile[4], 1);
  digitalWrite(Eile[6], 1);
  digitalWrite(Eile[9], 1);
  digitalWrite(Eile[11], 1);
  digitalWrite(Eile[12], 1);
  digitalWrite(Eile[14], 1);
  digitalWrite(Aukstas[2],0);
  delay(vidutinis);
  VisosIsjungtos();
 ///////////////////////////////////////////
  digitalWrite(Eile[0], 1);
  digitalWrite(Eile[2], 1);
  digitalWrite(Eile[5], 1);
  digitalWrite(Eile[7], 1);
  digitalWrite(Eile[8], 1);
  digitalWrite(Eile[10], 1);
  digitalWrite(Eile[13], 1);
  digitalWrite(Eile[15], 1);
  digitalWrite(Aukstas[1],0);
  delay(vidutinis);
VisosIsjungtos();
 ///////////////////////////////////////////
  digitalWrite(Eile[1], 1);
  digitalWrite(Eile[3], 1);
  digitalWrite(Eile[4], 1);
  digitalWrite(Eile[6], 1);
  digitalWrite(Eile[9], 1);
  digitalWrite(Eile[11], 1);
  digitalWrite(Eile[12], 1);
  digitalWrite(Eile[14], 1);
  digitalWrite(Aukstas[0],0);
  delay(vidutinis);
  VisosIsjungtos();

}

//********************************************************************************************//
void MirksiGeltonos() // Mirksi TIK geltonos lemputes.
{
  VisosIsjungtos();
  digitalWrite(Eile[1], 1);
  digitalWrite(Eile[3], 1);
  digitalWrite(Eile[4], 1);
  digitalWrite(Eile[6], 1);
  digitalWrite(Eile[9], 1);
  digitalWrite(Eile[11], 1);
  digitalWrite(Eile[12], 1);
  digitalWrite(Eile[14], 1);
  digitalWrite(Aukstas[3],0);
  delay(vidutinis);
VisosIsjungtos();
 ///////////////////////////////////////////
  digitalWrite(Eile[0], 1);
  digitalWrite(Eile[2], 1);
  digitalWrite(Eile[5], 1);
  digitalWrite(Eile[7], 1);
  digitalWrite(Eile[8], 1);
  digitalWrite(Eile[10], 1);
  digitalWrite(Eile[13], 1);
  digitalWrite(Eile[15], 1);
  digitalWrite(Aukstas[2],0);
  delay(vidutinis);
  VisosIsjungtos();
 ///////////////////////////////////////////
  digitalWrite(Eile[1], 1);
  digitalWrite(Eile[3], 1);
  digitalWrite(Eile[4], 1);
  digitalWrite(Eile[6], 1);
  digitalWrite(Eile[9], 1);
  digitalWrite(Eile[11], 1);
  digitalWrite(Eile[12], 1);
  digitalWrite(Eile[14], 1);
  digitalWrite(Aukstas[1],0);
  delay(vidutinis);
VisosIsjungtos();
 ///////////////////////////////////////////
  digitalWrite(Eile[0], 1);
  digitalWrite(Eile[2], 1);
  digitalWrite(Eile[5], 1);
  digitalWrite(Eile[7], 1);
  digitalWrite(Eile[8], 1);
  digitalWrite(Eile[10], 1);
  digitalWrite(Eile[13], 1);
  digitalWrite(Eile[15], 1);
  digitalWrite(Aukstas[0],0);
  delay(vidutinis);
  VisosIsjungtos();

}
//********************************************************************************************//
  void IjungtosRaudonos() // Mirksi TIK raudonos lemputes.
{
  VisosIsjungtos();
  digitalWrite(Eile[0], 1);
  digitalWrite(Eile[2], 1);
  digitalWrite(Eile[5], 1);
  digitalWrite(Eile[7], 1);
  digitalWrite(Eile[8], 1);
  digitalWrite(Eile[10], 1);
  digitalWrite(Eile[13], 1);
  digitalWrite(Eile[15], 1);
  digitalWrite(Aukstas[3],0);
  delay(zaibiskas);
VisosIsjungtos();
 ///////////////////////////////////////////
  digitalWrite(Eile[1], 1);
  digitalWrite(Eile[3], 1);
  digitalWrite(Eile[4], 1);
  digitalWrite(Eile[6], 1);
  digitalWrite(Eile[9], 1);
  digitalWrite(Eile[11], 1);
  digitalWrite(Eile[12], 1);
  digitalWrite(Eile[14], 1);
  digitalWrite(Aukstas[2],0);
  delay(zaibiskas);
  VisosIsjungtos();
 ///////////////////////////////////////////
  digitalWrite(Eile[0], 1);
  digitalWrite(Eile[2], 1);
  digitalWrite(Eile[5], 1);
  digitalWrite(Eile[7], 1);
  digitalWrite(Eile[8], 1);
  digitalWrite(Eile[10], 1);
  digitalWrite(Eile[13], 1);
  digitalWrite(Eile[15], 1);
  digitalWrite(Aukstas[1],0);
  delay(zaibiskas);
VisosIsjungtos();
 ///////////////////////////////////////////
  digitalWrite(Eile[1], 1);
  digitalWrite(Eile[3], 1);
  digitalWrite(Eile[4], 1);
  digitalWrite(Eile[6], 1);
  digitalWrite(Eile[9], 1);
  digitalWrite(Eile[11], 1);
  digitalWrite(Eile[12], 1);
  digitalWrite(Eile[14], 1);
  digitalWrite(Aukstas[0],0);
  delay(zaibiskas);
  VisosIsjungtos();

}
//********************************************************************************************//
void IjungtosGeltonos() // Ijungtos TIK geltonos lemputes.
{
  VisosIsjungtos();
  digitalWrite(Eile[1], 1);
  digitalWrite(Eile[3], 1);
  digitalWrite(Eile[4], 1);
  digitalWrite(Eile[6], 1);
  digitalWrite(Eile[9], 1);
  digitalWrite(Eile[11], 1);
  digitalWrite(Eile[12], 1);
  digitalWrite(Eile[14], 1);
  digitalWrite(Aukstas[3],0);
  delay(zaibiskas);
VisosIsjungtos();
 ///////////////////////////////////////////
  digitalWrite(Eile[0], 1);
  digitalWrite(Eile[2], 1);
  digitalWrite(Eile[5], 1);
  digitalWrite(Eile[7], 1);
  digitalWrite(Eile[8], 1);
  digitalWrite(Eile[10], 1);
  digitalWrite(Eile[13], 1);
  digitalWrite(Eile[15], 1);
  digitalWrite(Aukstas[2],0);
  delay(zaibiskas);
  VisosIsjungtos();
 ///////////////////////////////////////////
  digitalWrite(Eile[1], 1);
  digitalWrite(Eile[3], 1);
  digitalWrite(Eile[4], 1);
  digitalWrite(Eile[6], 1);
  digitalWrite(Eile[9], 1);
  digitalWrite(Eile[11], 1);
  digitalWrite(Eile[12], 1);
  digitalWrite(Eile[14], 1);
  digitalWrite(Aukstas[1],0);
  delay(zaibiskas);
VisosIsjungtos();
 ///////////////////////////////////////////
  digitalWrite(Eile[0], 1);
  digitalWrite(Eile[2], 1);
  digitalWrite(Eile[5], 1);
  digitalWrite(Eile[7], 1);
  digitalWrite(Eile[8], 1);
  digitalWrite(Eile[10], 1);
  digitalWrite(Eile[13], 1);
  digitalWrite(Eile[15], 1);
  digitalWrite(Aukstas[0],0);
  delay(zaibiskas);
  VisosIsjungtos();
}

void Test() // Patikrinamos visos lemputes (visos paeiliui po viena sumirksi).
{
  VisosIsjungtos();
	for (int k = 0; k < 4; k++)
	{
  digitalWrite(Aukstas[k], 0);
	 for (int i = 0; i < 16; i++)
	 {	 digitalWrite(Eile[i-1], 0);
		 digitalWrite(Eile[i], 1);
		 delay(labaigreitas);
	 }
   VisosIsjungtos();
	}
}	
