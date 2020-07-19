

/*-------------------------------------------------------------------------

		        Tetris Game 

Programmer           : Manish Kumar
Date                 : 05/02/2018
WEBSITE  : justdocodings.blogspot.in
Facebook : www.facebook.com/justdocodings
Twitter  : www.twitter.com/justdocodings

Check Out other programmes at https://justdocodings.blogspot.in

Software Details
====================
Developed in   : C++
Compiler used  : TC++ 3.0
OS             : Window 98,2000,XP,
		 Vista,Windows7(only safemode)

Licence   : Freeware (Please give the credit of programming to author.)


-------------------------------------------------------------------------------------*/



//***************************************************************
//                   Header file used in project
//****************************************************************

#include <conio.h>
#include <graphics.h>
#include <dos.h>
#include <stdlib.h>
#include <malloc.h>
#include <iostream.h>


// There are seven different types of tetrominoes : 

#define NONE 0
#define DESIGN_I 1 // O blocks
#define DESIGN_II 2 // T blocks
#define DESIGN_III 3 // I blocks
#define DESIGN_IV 4 // Z blocks
#define DESIGN_V 5 // S blocks
#define DESIGN_VI 6 // J blocks
#define DESIGN_VII 7 // L blocks


//***************************************************************
//                   Keys
//****************************************************************

#define LEFT 75
#define RIGHT 77
#define UP 72
#define DOWN 80
#define EXIT 27
#define SPACE 32

//***************************************************************
//                  
//****************************************************************

#define TRUE 1
#define FALSE 0

//***************************************************************************
//    These are used to check if the pattern can move - left, right or down.
//***************************************************************************

#define MOVELEFT 1
#define MOVERIGHT 2
#define MOVEDOWN 3

//***************************************************************
//          These are used to rotate DESIGN_III ( I blocks )
//****************************************************************


#define ANTICLOCKWISE 1
#define CLOCKWISE 2
#define NOTMOVE 0


//***************************************************************
//                   Global Variables
//****************************************************************

int X=120,Y=30,H=22,W=22;
int Tl=12,Th=20;
int Tetris[20][12],temp[20][12],colorInfo[20][12],tempColorInfo[20][12];
int start_x[4]={0}, start_y[4]={0};
int prev_x[4]={0},prev_y[4]={0},temp_x[4],temp_y[4];
int whichDesign=NONE, designColor=0, nextDesign=NONE;
int SPEED;
int center_x,center_y;
int Turn=1;
int clockAnti = NOTMOVE;

int score=0, level=1, lines=0;
char buffer[10];

int nextFlag=0;
int resetSpeed=FALSE;
int isGameOver=FALSE;
int disableSound=FALSE;


//***************************************************************
//    Function to define initial value of the pattern              
//****************************************************************

void InitDesign()
{

	switch(whichDesign)
	{
		case DESIGN_I:

		designColor=3;
		start_x[0]=(Tl/2)-1;
		start_x[1]=(Tl/2);
		start_x[2]=(Tl/2)-1;
		start_x[3]=(Tl/2);

		start_y[0]=1;
		start_y[1]=1;
		start_y[2]=2;
		start_y[3]=2;

		break;

		case DESIGN_II:

		designColor=4;
		start_x[0]=(Tl/2)-1;
		start_x[1]=(Tl/2)-2;
		start_x[2]=(Tl/2)-1;
		start_x[3]=(Tl/2);

		start_y[0]=1;
		start_y[1]=2;
		start_y[2]=2;
		start_y[3]=2;

		break;

		case DESIGN_III:

		designColor=12;
		start_x[0]=(Tl/2)-1;
		start_x[1]=(Tl/2)-1;
		start_x[2]=(Tl/2)-1;
		start_x[3]=(Tl/2)-1;

		start_y[0]=0;
		start_y[1]=1;
		start_y[2]=2;
		start_y[3]=3;

		break;

		case DESIGN_IV:

		designColor=1;
		start_x[0]=(Tl/2)-2;
		start_x[1]=(Tl/2)-1;
		start_x[2]=(Tl/2)-1;
		start_x[3]=(Tl/2);

		start_y[0]=1;
		start_y[1]=1;
		start_y[2]=2;
		start_y[3]=2;

		break;

		case DESIGN_V:

		designColor=2;
		start_x[0]=(Tl/2)-1;
		start_x[1]=(Tl/2);
		start_x[2]=(Tl/2)-2;
		start_x[3]=(Tl/2)-1;

		start_y[0]=1;
		start_y[1]=1;
		start_y[2]=2;
		start_y[3]=2;

		break;

		case DESIGN_VI:

		designColor=9;
		start_x[0]=(Tl/2);
		start_x[1]=(Tl/2)-2;
		start_x[2]=(Tl/2)-1;
		start_x[3]=(Tl/2);

		start_y[0]=1;
		start_y[1]=2;
		start_y[2]=2;
		start_y[3]=2;

		break;

		case DESIGN_VII:

		designColor=14;
		start_x[0]=(Tl/2)-2;
		start_x[1]=(Tl/2)-2;
		start_x[2]=(Tl/2)-1;
		start_x[3]=(Tl/2);

		start_y[0]=1;
		start_y[1]=2;
		start_y[2]=2;
		start_y[3]=2;

		break;
	}

	for(int i=0;i<4;i++)
	{
		Tetris[start_y[i]][start_x[i]]=TRUE;
		colorInfo[start_y[i]][start_x[i]]=designColor;
	}


}

//***************************************************************
//           Function to design Background
//****************************************************************

void InitBackground()
{

	setfillstyle(SOLID_FILL,0);
	bar(0,0,640,480);

	for(int j=0;j<3000;j++)
			putpixel(random(640),random(480),random(16));

	setfillstyle(SOLID_FILL,15);
	bar(X,Y,X+(Tl*W),Y+(Th*H));
	setcolor(14);
	rectangle(X-1,Y-1,X+(Tl*W)+1,Y+(Th*H)+1);
	setcolor(2);
	rectangle(X-2,Y-2,X+(Tl*W)+2,Y+(Th*H)+2);
	setcolor(12);
	rectangle(X-3,Y-3,X+(Tl*W)+3,Y+(Th*H)+3);
	setcolor(14);
	rectangle(X-4,Y-4,X+(Tl*W)+4,Y+(Th*H)+4);

       setfillstyle(SOLID_FILL,11);
       bar(X+(Tl*W)+7,Y-1,X+(Tl*W)+4*W+(4*W),Y+(5*H));

       setfillstyle(SOLID_FILL,14);
       bar(X+(Tl*W)+7,Y+(5*H)+2,X+(Tl*W)+4*W+(4*W),Y+(10*H));

       setfillstyle(SOLID_FILL,10);
       bar(X+(Tl*W)+7,Y+(10*H)+2,X+(Tl*W)+4*W+(4*W),Y+(15*H));

       setfillstyle(SOLID_FILL,12);
       bar(X+(Tl*W)+7,Y+(15*H)+2,X+(Tl*W)+4*W+(4*W),Y+(20*H)+3);

       setcolor(13);
       rectangle(X+(Tl*W)+5,Y-4,X+(Tl*W)+4*W+4*W+1,Y+20*H+4);

       settextstyle(0,0,2);
       setcolor(8);
       outtextxy(X+(Tl*W)+7+2*W,Y+(5*H)+2+H,"Score");
       outtextxy(X+(Tl*W)+7+2*W,Y+(10*H)+2+H,"Level");
       outtextxy(X+(Tl*W)+7+2*W,Y+(15*H)+2+H,"Lines");

       setcolor(0);

       outtextxy(X+(Tl*W)+7+3*W,Y+(5*H)+2+3*H,itoa(score,buffer,10));
       outtextxy(X+(Tl*W)+7+3*W,Y+(10*H)+2+3*H,itoa(level,buffer,10));
       outtextxy(X+(Tl*W)+7+3*W,Y+(15*H)+2+3*H,itoa(lines,buffer,10));

       settextstyle(0,0,0);

}

//***************************************************************
//         Function to design a pattern          
//****************************************************************

void Draw()
{
	int c=0;

	setcolor(c);
	setfillstyle(SOLID_FILL,designColor);
	rectangle(X+(start_x[0]*W),Y+(start_y[0]*H),X+(start_x[0]*W)+W,Y+(start_y[0]*H)+H);
	floodfill(X+(start_x[0]*W)+1,Y+(start_y[0]*H)+1,c);

	setcolor(c);
	setfillstyle(SOLID_FILL,designColor);
	rectangle(X+(start_x[1]*W),Y+(start_y[1]*H),X+(start_x[1]*W)+W,Y+(start_y[1]*H)+H);
	floodfill(X+(start_x[1]*W)+1,Y+(start_y[1]*H)+1,c);

	setcolor(c);
	setfillstyle(SOLID_FILL,designColor);
	rectangle(X+(start_x[2]*W),Y+(start_y[2]*H),X+(start_x[2]*W)+W,Y+(start_y[2]*H)+H);
	floodfill(X+(start_x[2]*W)+1,Y+(start_y[2]*H)+1,c);

	setcolor(c);
	setfillstyle(SOLID_FILL,designColor);
	rectangle(X+(start_x[3]*W),Y+(start_y[3]*H),X+(start_x[3]*W)+W,Y+(start_y[3]*H)+H);
	floodfill(X+(start_x[3]*W)+1,Y+(start_y[3]*H)+1,c);

}

//***************************************************************
//  Function to design next pattern                  
//****************************************************************

void drawNextPattern(int Xpos, int Ypos)
{
	
	int c=0;
	int next_x[4],next_y[4];
	int pColor=0;

	/*-------------------------------------------------------------------*/
	
	
	switch(nextDesign)
	{
		case DESIGN_I:

		pColor=3;
		next_x[0]=(Tl/2)-1;
		next_x[1]=(Tl/2);
		next_x[2]=(Tl/2)-1;
		next_x[3]=(Tl/2);

		next_y[0]=1;
		next_y[1]=1;
		next_y[2]=2;
		next_y[3]=2;

		break;

		case DESIGN_II:

		pColor=4;
		next_x[0]=(Tl/2)-1;
		next_x[1]=(Tl/2)-2;
		next_x[2]=(Tl/2)-1;
		next_x[3]=(Tl/2);

		next_y[0]=1;
		next_y[1]=2;
		next_y[2]=2;
		next_y[3]=2;

		break;

		case DESIGN_III:

		pColor=12;
		next_x[0]=(Tl/2)-1;
		next_x[1]=(Tl/2)-1;
		next_x[2]=(Tl/2)-1;
		next_x[3]=(Tl/2)-1;

		next_y[0]=0;
		next_y[1]=1;
		next_y[2]=2;
		next_y[3]=3;

		break;

		case DESIGN_IV:

		pColor=1;
		next_x[0]=(Tl/2)-2;
		next_x[1]=(Tl/2)-1;
		next_x[2]=(Tl/2)-1;
		next_x[3]=(Tl/2);

		next_y[0]=1;
		next_y[1]=1;
		next_y[2]=2;
		next_y[3]=2;

		break;

		case DESIGN_V:

		pColor=2;
		next_x[0]=(Tl/2)-1;
		next_x[1]=(Tl/2);
		next_x[2]=(Tl/2)-2;
		next_x[3]=(Tl/2)-1;

		next_y[0]=1;
		next_y[1]=1;
		next_y[2]=2;
		next_y[3]=2;

		break;

		case DESIGN_VI:

		pColor=9;
		next_x[0]=(Tl/2);
		next_x[1]=(Tl/2)-2;
		next_x[2]=(Tl/2)-1;
		next_x[3]=(Tl/2);

		next_y[0]=1;
		next_y[1]=2;
		next_y[2]=2;
		next_y[3]=2;

		break;

		case DESIGN_VII:

		pColor=14;
		next_x[0]=(Tl/2)-2;
		next_x[1]=(Tl/2)-2;
		next_x[2]=(Tl/2)-1;
		next_x[3]=(Tl/2);

		next_y[0]=1;
		next_y[1]=2;
		next_y[2]=2;
		next_y[3]=2;

		break;
	}
	
	
	/*--------------------------------------------------------------------*/



	setcolor(c);
	setfillstyle(SOLID_FILL,pColor);
	rectangle(Xpos+(next_x[0]*W),Ypos+(next_y[0]*H),Xpos+(next_x[0]*W)+W,Ypos+(next_y[0]*H)+H);
	floodfill(Xpos+(next_x[0]*W)+1,Ypos+(next_y[0]*H)+1,c);

	setcolor(c);
	setfillstyle(SOLID_FILL,pColor);
	rectangle(Xpos+(next_x[1]*W),Ypos+(next_y[1]*H),Xpos+(next_x[1]*W)+W,Ypos+(next_y[1]*H)+H);
	floodfill(Xpos+(next_x[1]*W)+1,Ypos+(next_y[1]*H)+1,c);

	setcolor(c);
	setfillstyle(SOLID_FILL,pColor);
	rectangle(Xpos+(next_x[2]*W),Ypos+(next_y[2]*H),Xpos+(next_x[2]*W)+W,Ypos+(next_y[2]*H)+H);
	floodfill(Xpos+(next_x[2]*W)+1,Ypos+(next_y[2]*H)+1,c);

	setcolor(c);
	setfillstyle(SOLID_FILL,pColor);
	rectangle(Xpos+(next_x[3]*W),Ypos+(next_y[3]*H),Xpos+(next_x[3]*W)+W,Ypos+(next_y[3]*H)+H);
	floodfill(Xpos+(next_x[3]*W)+1,Ypos+(next_y[3]*H)+1,c);
	
}

//***************************************************************
//      Function to clear the pattern             
//****************************************************************

void Clear()
{
	setfillstyle(SOLID_FILL,15);
	bar(X+(prev_x[0]*W),Y+(prev_y[0]*H),X+(prev_x[0]*W)+W,Y+(prev_y[0]*H)+H);
	bar(X+(prev_x[1]*W),Y+(prev_y[1]*H),X+(prev_x[1]*W)+W,Y+(prev_y[1]*H)+H);
	bar(X+(prev_x[2]*W),Y+(prev_y[2]*H),X+(prev_x[2]*W)+W,Y+(prev_y[2]*H)+H);
	bar(X+(prev_x[3]*W),Y+(prev_y[3]*H),X+(prev_x[3]*W)+W,Y+(prev_y[3]*H)+H);
}

//***************************************************************
//   Function to move the pattern in left direction                
//****************************************************************

void moveLeft()
{
	for(int _i=0;_i<4;_i++)
	{
		prev_x[_i]=start_x[_i];
		prev_y[_i]=start_y[_i];
		Tetris[start_y[_i]][start_x[_i]]=FALSE;
		colorInfo[start_y[_i]][start_x[_i]]=NONE;
	}

	for(int i=0;i<4;i++)
	{
		start_x[i]-=1;
		Tetris[start_y[i]][start_x[i]]=TRUE;
		colorInfo[start_y[i]][start_x[i]]=designColor;
	}
	Clear();
	Draw();
}

//***************************************************************
//   Function to move the pattern in right direction                
//****************************************************************

void moveRight()
{

	for(int _i=0;_i<4;_i++)
	{
		prev_x[_i]=start_x[_i];
		prev_y[_i]=start_y[_i];
		Tetris[start_y[_i]][start_x[_i]]=FALSE;
		colorInfo[start_y[_i]][start_x[_i]]=NONE;
	}

	for(int i=0;i<4;i++)
	{
		start_x[i]+=1;
		Tetris[start_y[i]][start_x[i]]=TRUE;
		colorInfo[start_y[i]][start_x[i]]=designColor;
	}
	Clear();
	Draw();
}

//***************************************************************
//   Function to move the pattern down    
//****************************************************************

void moveDown()
{

	for(int _i=0;_i<4;_i++)
	{
		prev_x[_i]=start_x[_i];
		prev_y[_i]=start_y[_i];
		Tetris[start_y[_i]][start_x[_i]]=FALSE;
		colorInfo[start_y[_i]][start_x[_i]]=NONE;
	}	
	
	for(int i=0;i<4;i++)
	{
		start_y[i]+=1;
		Tetris[start_y[i]][start_x[i]]=TRUE;
		colorInfo[start_y[i]][start_x[i]]=designColor;
	}
	Clear();
	Draw();
}
/*-------------------------------------------------------------------------------
    It checks that the pattern collides with any pattern or border of the game 
---------------------------------------------------------------------------------*/
int check_x(int border)
{
	if(start_x[0]==border||start_x[1]==border||start_x[2]==border||start_x[3]==border)
		return TRUE;
	return FALSE;
}

int check_y(int border)
{
	if(start_y[0]==border||start_y[1]==border||start_y[2]==border||start_y[3]==border)
		return TRUE;
	return FALSE;
}

/**********************************************/


/*-------------------------------------------------------------------------------
    These function checks that the pattern can move left, right or down.
---------------------------------------------------------------------------------*/

int check(int a, int b)
{
	for(int i=0;i<4;i++)
	{
		if(temp_x[i]==a&&temp_y[i]==b)
			return TRUE;
	}
	return FALSE;
}

int checkCollision(int movement)
{

	for(int l=0;l<4;l++)
	{
		temp_x[l]=start_x[l];
		temp_y[l]=start_y[l];
	}

	switch(movement)
	{
		//Right
		case MOVERIGHT:
		for(int i=0;i<4;i++)
		{
			if(Tetris[start_y[i]][start_x[i]+1]==TRUE && check(start_x[i]+1,start_y[i])==FALSE)
				return TRUE;
		}
		break;
		//Left
		case MOVELEFT:
		for(int j=0;j<4;j++)
		{
			if(Tetris[start_y[j]][start_x[j]-1]==TRUE && check(start_x[j]-1,start_y[j])==FALSE)
				return TRUE;
		}
		break;
		//Down
		case MOVEDOWN:
		for(int k=0;k<4;k++)
		{

			if(Tetris[start_y[k]+1][start_x[k]]==TRUE && check(start_x[k],start_y[k]+1)==FALSE)
				return TRUE;
		}
		break;
	}


	return FALSE;
}

/* This function is used for DESIGN_III( I blocks) */

int readyToMove(int x, int y)
{

	if(Tetris[y][x-1]==FALSE && Tetris[y][x-2]==FALSE && (x-1)>=0&&(x-2>=0))
		return ANTICLOCKWISE;
	if(Tetris[y][x+1]==FALSE && Tetris[y][x+2]==FALSE && (x+1<=11)&&(x+2<=11))
		return CLOCKWISE;

	return NOTMOVE;
}

//***************************************************************
//   Function to draw a 3D Text
//****************************************************************

void Text3D(int x, int y, int depth, int bgcolor, int fgcolor, char *caption)
{
	int i;
	setcolor(bgcolor);
	for(i=0;i<depth;i++)
		outtextxy(x+i,y+i,caption);
	setcolor(fgcolor);
	outtextxy(x+i,y+i,caption);

}


//***************************************************************
//   Function to Draw Logo    
//****************************************************************

void JClogo()
{


  /*********** Logo ************/

    setcolor(3);
    setfillstyle(SOLID_FILL,3);
    circle(280,180,30);
    floodfill(280,180,3);

    setcolor(15);
    setfillstyle(SOLID_FILL,15);
    circle(280,180,27);
    circle(280,180,24);
    floodfill(254,180,15);

    settextstyle(1,0,4);
    outtextxy(265,160,"JC");
  /******************************/

    setcolor(15);
    settextstyle(0,0,2);
    Text3D(200,240,2,3,11,"Just Coding");
    Text3D(220,290,2,3,11,"Presents");
    Text3D(70,390,2,3,11,"www.justdocodings.blogspot.in");

    settextstyle(0,0,0);

}

//***************************************************************
//   Starting Screen    
//****************************************************************

void Start()
{


   settextstyle(0,0,2);
   Text3D(230,200,2,3,11,"Loading...");
   settextstyle(0,0,0);
   for(int i=0;i<1000;i++)
	putpixel(random(640),random(480),random(16));
   delay(4000);
   cleardevice();

   JClogo();
   for(int l=0;l<1000;l++)
	putpixel(random(640),random(480),random(16));

   delay(5000);
   cleardevice();

   settextstyle(0,0,2);
   Text3D(230,200,2,3,11,"a game by");
   Text3D(250,240,2,3,11,"Manish Kumar");
   settextstyle(0,0,0);
   for(int k=0;k<1000;k++)
	putpixel(random(640),random(480),random(16));

   delay(4000);
   cleardevice();

   settextstyle(0,0,7);
   Text3D(150,150,4,3,11,"TETRIS");
   settextstyle(0,0,2);
   Text3D(100,300,2,3,11,"(c) Copyright 2018 Manish Kumar");
   settextstyle(0,0,0);
   for(int j=0;j<2000;j++)
	putpixel(random(640),random(480),random(16));
   delay(6000);
   cleardevice();


}

//***************************************************************
//   Introduction Function
//****************************************************************

void Intro()
{

   cleardevice();
   setcolor(15);
   settextstyle(0,0,4);
   for(int i=0;i<4;i++)
   outtextxy(260+i,30+i,"HELP");
   settextstyle(0,0,2);
   setcolor(4);
   for(int k=0;k<=3;k++)
   {
	outtextxy(100+k,100+30-k,"Left  Key  : Move Left");
	outtextxy(100+k,130+30-k,"Right Key  : Move Right");
	outtextxy(100+k,160+30-k,"Up    Key  : Rotate");
	outtextxy(100+k,190+30-k,"Down  Key  : Increase Speed");
	outtextxy(100+k,220+30-k,"Space      : Pause");
	outtextxy(100+k,250+30-k,"Esc        : Return");
	outtextxy(100+k,280+30-k,"S          : Pause Sound");

	outtextxy(100+k,380+30-k,"Press any key to continue...");
	if(k==2)
	setcolor(12);
   }
   for(int _i=0;_i<1000;_i++)
	putpixel(random(640),random(480),random(16));
   getch();
}

//***************************************************************
//   Function to rotate a pattern
//****************************************************************

void rotateShapes()
{
	int canMove=FALSE;

	switch(whichDesign)
	{
		case 1:
		break;

		case 2:
		{

			if(checkCollision(MOVELEFT)==TRUE&&checkCollision(MOVERIGHT)==TRUE&&(Turn==2||Turn==4))
			{
			}
			
			else 
			{

				canMove=TRUE;
				center_x=start_x[2];
				center_y=start_y[2];

				
				for(int _i=0;_i<4;_i++)
				{
					prev_x[_i]=start_x[_i];
					prev_y[_i]=start_y[_i];
					Tetris[start_y[_i]][start_x[_i]]=FALSE;
					colorInfo[start_y[_i]][start_x[_i]]=NONE;
				}

				/***************************************************/

				if((center_x==Tl-1 && checkCollision(MOVELEFT)==FALSE) || (Tetris[center_y][center_x+1]==TRUE&&checkCollision(MOVELEFT)==FALSE))
				{
					for(int i=0;i<4;i++)
						start_x[i]-=1;

				}
				else if((center_x==0 && checkCollision(MOVERIGHT)==FALSE) || (Tetris[center_y][center_x-1]==TRUE&&checkCollision(MOVERIGHT)==FALSE))
				{
					for(int i=0;i<4;i++)
						start_x[i]+=1;

				}



			/***************************************************/



				if(Turn==1)
				{
					start_x[0]+=1;
					start_y[0]+=1;
					start_x[1]+=1;
					start_y[1]-=1;
					start_x[3]-=1;
					start_y[3]+=1;
					
					Turn=2;

				}

				else if(Turn==2)
				{
					start_x[0]-=1;
					start_y[0]+=1;
					start_x[1]+=1;
					start_y[1]+=1;
					start_x[3]-=1;
					start_y[3]-=1;
					
					Turn=3;
				}

				else if(Turn==3)
				{
					start_x[0]-=1;
					start_y[0]-=1;
					start_x[1]-=1;
					start_y[1]+=1;
					start_x[3]+=1;
					start_y[3]-=1;
					
					Turn = 4;

				}

				else if(Turn==4)
				{
					start_x[0]+=1;
					start_y[0]-=1;
					start_x[1]-=1;
					start_y[1]-=1;
					start_x[3]+=1;
					start_y[3]+=1;
					
					Turn = 1;

				}
			}


		}
		break;

		case 3:

		{
			if(checkCollision(MOVELEFT)==TRUE&&checkCollision(MOVERIGHT)==TRUE&&Turn==1)
			{
			}

			else
			{

				canMove=TRUE;
				center_x=start_x[2];
				center_y=start_y[2];


				for(int _i=0;_i<4;_i++)
				{
					prev_x[_i]=start_x[_i];
					prev_y[_i]=start_y[_i];
					Tetris[start_y[_i]][start_x[_i]]=FALSE;
					colorInfo[start_y[_i]][start_x[_i]]=NONE;
				}

				/***************************************************/

				if((center_x==Tl-1 && checkCollision(MOVELEFT)==FALSE) || (Tetris[center_y][center_x+1]==TRUE&&checkCollision(MOVELEFT)==FALSE))
				{
					for(int i=0;i<4;i++)
						start_x[i]-=1;
					center_x=start_x[2];
				}
				else if((center_x==0 && checkCollision(MOVERIGHT)==FALSE) || (Tetris[center_y][center_x-1]==TRUE&&checkCollision(MOVERIGHT)==FALSE))
				{
					for(int i=0;i<4;i++)
						start_x[i]+=1;
					center_x=start_x[2];
				}

				
				
				if(Turn==1)
				clockAnti=readyToMove(center_x,center_y);

				if(clockAnti==NOTMOVE)
				{
					canMove=FALSE;
					for(int _i=0;_i<4;_i++)
					{
						start_x[_i]=prev_x[_i];
						start_y[_i]=prev_y[_i];
						Tetris[start_y[_i]][start_x[_i]]=TRUE;
						colorInfo[start_y[_i]][start_x[_i]]=designColor;
					}

				}
				else if(clockAnti==ANTICLOCKWISE)
				{
					if(Turn==1)
					{
						start_x[0]-=2;
						start_y[0]+=2;
						start_x[1]-=1;
						start_y[1]+=1;
						start_x[3]+=1;
						start_y[3]-=1;


						Turn=2;
					}
					else if(Turn==2)
					{
						start_x[0]+=2;
						start_y[0]-=2;
						start_x[1]+=1;
						start_y[1]-=1;
						start_x[3]-=1;
						start_y[3]+=1;

						Turn=1;
					}
				}
				else if(clockAnti==CLOCKWISE)
				{
					if(Turn==1)
					{
						start_x[0]+=2;
						start_y[0]+=2;
						start_x[1]+=1;
						start_y[1]+=1;
						start_x[3]-=1;
						start_y[3]-=1;


						Turn=2;
					}
					else if(Turn==2)
					{
						start_x[0]-=2;
						start_y[0]-=2;
						start_x[1]-=1;
						start_y[1]-=1;
						start_x[3]+=1;
						start_y[3]+=1;

						Turn=1;
					}
				}

			/***************************************************/






			}
		}
		
		/*-----------------------------------------------------------------------*/
		break;
		case 4:
		{
			if(checkCollision(MOVELEFT)==TRUE&&checkCollision(MOVERIGHT)==TRUE&&Turn==2)
			{
			}
			
			else
			{

				canMove=TRUE;
				center_x=start_x[2];
				center_y=start_y[2];


				for(int _i=0;_i<4;_i++)
				{
					prev_x[_i]=start_x[_i];
					prev_y[_i]=start_y[_i];
					Tetris[start_y[_i]][start_x[_i]]=FALSE;
					colorInfo[start_y[_i]][start_x[_i]]=NONE;
				}

				/***************************************************/

				if((center_x==Tl-1 && checkCollision(MOVELEFT)==FALSE) || (Tetris[center_y][center_x+1]==TRUE&&checkCollision(MOVELEFT)==FALSE))
				{
					for(int i=0;i<4;i++)
						start_x[i]-=1;

				}
				else if((center_x==0 && checkCollision(MOVERIGHT)==FALSE) || (Tetris[center_y][center_x-1]==TRUE&&checkCollision(MOVERIGHT)==FALSE))
				{
					for(int i=0;i<4;i++)
						start_x[i]+=1;

				}



			/***************************************************/

				if(Turn==1)
				{
					start_x[0]+=2;
					start_x[1]+=1;
					start_y[1]+=1;
					start_x[3]-=1;
					start_y[3]+=1;


					Turn=2;
				}
				else if(Turn==2)
				{
					start_x[0]-=2;
					start_x[1]-=1;
					start_y[1]-=1;
					start_x[3]+=1;
					start_y[3]-=1;

					Turn=1;
				}




			}
		}
		break;
		case 5:
		{
			if(checkCollision(MOVELEFT)==TRUE&&checkCollision(MOVERIGHT)==TRUE&&Turn==2)
			{
			}

			else
			{

				canMove=TRUE;
				center_x=start_x[0];
				center_y=start_y[0];


				for(int _i=0;_i<4;_i++)
				{
					prev_x[_i]=start_x[_i];
					prev_y[_i]=start_y[_i];
					Tetris[start_y[_i]][start_x[_i]]=FALSE;
					colorInfo[start_y[_i]][start_x[_i]]=NONE;
				}
				
				/***************************************************/

				if((center_x==Tl-1 && checkCollision(MOVELEFT)==FALSE) || (Tetris[center_y][center_x+1]==TRUE&&checkCollision(MOVELEFT)==FALSE))
				{
					for(int i=0;i<4;i++)
						start_x[i]-=1;

				}
				else if((center_x==0 && checkCollision(MOVERIGHT)==FALSE) || (Tetris[center_y][center_x-1]==TRUE&&checkCollision(MOVERIGHT)==FALSE))
				{
					for(int i=0;i<4;i++)
						start_x[i]+=1;

				}



			/***************************************************/

				if(Turn==1)
				{
					start_x[1]-=1;
					start_y[1]-=1;
					start_x[2]+=2;
					start_x[3]+=1;
					start_y[3]-=1;


					Turn=2;
				}
				else if(Turn==2)
				{

					start_x[1]+=1;
					start_y[1]+=1;
					start_x[2]-=2;
					start_x[3]-=1;
					start_y[3]+=1;

					Turn=1;
				}




			}
		}
		break;
		case 6:
		{
			if(checkCollision(MOVELEFT)==TRUE&&checkCollision(MOVERIGHT)==TRUE&&(Turn==2||Turn==4))
			{
			}

			else
			{

				canMove=TRUE;
				center_x=start_x[2];
				center_y=start_y[2];


				for(int _i=0;_i<4;_i++)
				{
					prev_x[_i]=start_x[_i];
					prev_y[_i]=start_y[_i];
					Tetris[start_y[_i]][start_x[_i]]=FALSE;
					colorInfo[start_y[_i]][start_x[_i]]=NONE;
				}

				/***************************************************/

				if((center_x==Tl-1 && checkCollision(MOVELEFT)==FALSE) || (Tetris[center_y][center_x+1]==TRUE&&checkCollision(MOVELEFT)==FALSE))
				{
					for(int i=0;i<4;i++)
						start_x[i]-=1;

				}
				else if((center_x==0 && checkCollision(MOVERIGHT)==FALSE) || (Tetris[center_y][center_x-1]==TRUE&&checkCollision(MOVERIGHT)==FALSE))
				{
					for(int i=0;i<4;i++)
						start_x[i]+=1;

				}



			/***************************************************/



				if(Turn==1)
				{
					start_y[0]+=2;
					start_x[3]-=1;
					start_y[3]+=1;
					start_x[1]+=1;
					start_y[1]-=1;

					Turn=2;

				}

				else if(Turn==2)
				{
					start_x[0]-=2;
					start_x[3]-=1;
					start_y[3]-=1;
					start_x[1]+=1;
					start_y[1]+=1;

					Turn=3;
				}

				else if(Turn==3)
				{
					start_y[0]-=2;
					start_x[3]+=1;
					start_y[3]-=1;
					start_x[1]-=1;
					start_y[1]+=1;

					Turn = 4;

				}

				else if(Turn==4)
				{
					start_x[0]+=2;
					start_x[3]+=1;
					start_y[3]+=1;
					start_x[1]-=1;
					start_y[1]-=1;

					Turn = 1;

				}
			}

		}

		break;

		case 7:
		{
			if(checkCollision(MOVELEFT)==TRUE&&checkCollision(MOVERIGHT)==TRUE&&(Turn==2||Turn==4))
			{
			}

			else
			{

				canMove=TRUE;
				center_x=start_x[2];
				center_y=start_y[2];


				for(int _i=0;_i<4;_i++)
				{
					prev_x[_i]=start_x[_i];
					prev_y[_i]=start_y[_i];
					Tetris[start_y[_i]][start_x[_i]]=FALSE;
					colorInfo[start_y[_i]][start_x[_i]]=NONE;
				}

				/***************************************************/

				if((center_x==Tl-1 && checkCollision(MOVELEFT)==FALSE) || (Tetris[center_y][center_x+1]==TRUE&&checkCollision(MOVELEFT)==FALSE))
				{
					for(int i=0;i<4;i++)
						start_x[i]-=1;
							
				}
				else if((center_x==0 && checkCollision(MOVERIGHT)==FALSE) || (Tetris[center_y][center_x-1]==TRUE&&checkCollision(MOVERIGHT)==FALSE))
				{
					for(int i=0;i<4;i++)
						start_x[i]+=1;

				}



			/***************************************************/



				if(Turn==1)
				{
					start_x[0]+=2;
					start_x[1]+=1;
					start_y[1]-=1;
					start_x[3]-=1;
					start_y[3]+=1;

					Turn=2;

				}

				else if(Turn==2)
				{
					start_y[0]+=2;
					start_x[1]+=1;
					start_y[1]+=1;
					start_x[3]-=1;
					start_y[3]-=1;

					Turn=3;
				}

				else if(Turn==3)
				{
					start_x[0]-=2;
					start_x[1]-=1;
					start_y[1]+=1;
					start_x[3]+=1;
					start_y[3]-=1;

					Turn = 4;

				}

				else if(Turn==4)
				{
					start_y[0]-=2;
					start_x[1]-=1;
					start_y[1]-=1;
					start_x[3]+=1;
					start_y[3]+=1;

					Turn = 1;

				}
			}

		}
		break;
	}

	if(canMove)
	{
		/*
		   If start_y contains any value  greater than 19
		   then correct it.
		*/

		{
			int flag=0,gNum=0;
			for(int i=0;i<4;i++)
				if(start_y[i]>19)
				{
					if(gNum<start_y[i])
						gNum=start_y[i];
					flag=1;
				}
				if(flag==1)
				{
					for(int i=0;i<4;i++)
						start_y[i]-=gNum-19;
				}

		}

		/*
			If start_y overrides existing block i.e. it contanins the
			position which is already true in Tetris[...][...] then correct it. */


		{
			int flag=0;
			for(int i=0;i<4;i++)

				if(Tetris[start_y[i]][start_x[i]]==TRUE)
					flag=1;

				if(flag==1)
				{
					for(int i=0;i<4;i++)
						start_y[i]-=1;
				}

		}


		for(int j=0;j<4;j++)
		{	
			Tetris[start_y[j]][start_x[j]]=TRUE;
			colorInfo[start_y[j]][start_x[j]]=designColor;
		}	

		Clear();
		Draw();
	}



}

//***************************************************************
//   Function to check that line is completed or not.
//****************************************************************

void lineCompleted()
{
	int flag=0, updateScreen=0;
	int i=Th-1;
	for(i=Th-1;i>=0;i--)
	{
		for(int j=0;j<Tl;j++)
		{
			if(Tetris[i][j]==TRUE)
				flag=1;
			else
			{
				flag=0;
				break;
			}

		}

		

		if(flag==1)
		{

		lines++;
		score+=level;
	    flag=0;
		updateScreen=1;
			

			/* Swapping Starts */

			for(int k=0;k<i;k++)
				for(int l=0;l<Tl;l++)
				{	
					temp[k+1][l]=Tetris[k][l];
					tempColorInfo[k+1][l]=colorInfo[k][l];
				}	
				

			for(int m=Th-1;m>=i+1;m--)
					for(int n=0;n<Tl;n++)
					{
						temp[m][n]=Tetris[m][n];
						tempColorInfo[m][n]=colorInfo[m][n];
					}

			

			for(int y=0;y<Th;y++)
				for(int x=0;x<Tl;x++)
				{	
						Tetris[y][x]=temp[y][x];
						colorInfo[y][x]=tempColorInfo[y][x];
				}

			/*-------------------------------*/

			i=Th-1;
			for(int r=0;r<Th;r++)
				for(int s=0;s<Tl;s++)
				{
					temp[r][s]=0;
					tempColorInfo[r][s]=0;
				}

		}


	}

	/* Draw Image */

	if(updateScreen==1)
	{

		setfillstyle(SOLID_FILL,15);
		bar(X,Y,X+(Tl*W),Y+(Th*H));

		for(int i=0;i<Th;i++)
		{
			for(int j=0;j<Tl;j++)
			{
				if(Tetris[i][j]==TRUE)
				{
					setcolor(0);
					setfillstyle(SOLID_FILL,colorInfo[i][j]);
					rectangle(X+j*W,Y+i*H,X+j*W+W,Y+i*H+H);
					floodfill(X+(j*W)+3,Y+(i*H)+3,0);
				}
				else
				{
					setfillstyle(SOLID_FILL,15);
					bar(X+j*W,Y+i*H,X+j*W+W,Y+i*H+H);
				}
			}
		 }

	}


}

//***************************************************************
//   Function to update lines, score and level
//****************************************************************

void updateData()
{

       setfillstyle(SOLID_FILL,11);
       bar(X+(Tl*W)+7,Y-1,X+(Tl*W)+4*W+(4*W),Y+(5*H));

       setfillstyle(SOLID_FILL,14);
       bar(X+(Tl*W)+7,Y+(5*H)+2,X+(Tl*W)+4*W+(4*W),Y+(10*H));

       setfillstyle(SOLID_FILL,10);
       bar(X+(Tl*W)+7,Y+(10*H)+2,X+(Tl*W)+4*W+(4*W),Y+(15*H));

       setfillstyle(SOLID_FILL,12);
       bar(X+(Tl*W)+7,Y+(15*H)+2,X+(Tl*W)+4*W+(4*W),Y+(20*H)+3);

       setcolor(13);
       rectangle(X+(Tl*W)+5,Y-4,X+(Tl*W)+4*W+4*W+1,Y+20*H+4);

       settextstyle(0,0,2);
       setcolor(8);
       outtextxy(X+(Tl*W)+7+2*W,Y+(5*H)+2+H,"Score");
       outtextxy(X+(Tl*W)+7+2*W,Y+(10*H)+2+H,"Level");
       outtextxy(X+(Tl*W)+7+2*W,Y+(15*H)+2+H,"Lines");

       setcolor(0);

       outtextxy(X+(Tl*W)+7+3*W,Y+(5*H)+2+3*H,itoa(score,buffer,10));
       outtextxy(X+(Tl*W)+7+3*W,Y+(10*H)+2+3*H,itoa(level,buffer,10));
       outtextxy(X+(Tl*W)+7+3*W,Y+(15*H)+2+3*H,itoa(lines,buffer,10));
       settextstyle(0,0,2);

}

//***************************************************************
//   Function to draw Main Menu
//****************************************************************

void mainMenu()
{
	int _x=220,_y=50,_h=30;
	int cY=_y+2*_h;
	int choice=1;
	int key;
	cleardevice();
	do{

		settextstyle(0,0,4);
		Text3D(_x-70,_y,2,3,11,"MAIN MENU");
		settextstyle(0,0,2);
		Text3D(_x,_y+2*_h,1,3,11,"1.  Level 1");
		Text3D(_x,_y+3*_h,1,3,11,"2.  Level 2");
		Text3D(_x,_y+4*_h,1,3,11,"3.  Level 3");
		Text3D(_x,_y+5*_h,1,3,11,"4.  Level 4");
		Text3D(_x,_y+6*_h,1,3,11,"5.  Level 5");
		Text3D(_x,_y+7*_h,1,3,11,"6.  Level 6");
		Text3D(_x,_y+8*_h,1,3,11,"7.  Level 7");
		Text3D(_x,_y+9*_h,1,3,11,"8.  Level 8");
		Text3D(_x,_y+10*_h,1,3,11,"9.  Level 9");
		Text3D(_x,_y+11*_h,1,3,11,"10. Level 10");
		Text3D(_x,_y+12*_h,1,3,11,"11. Exit");
		for(int j=0;j<3000;j++)
			putpixel(random(640),random(480),random(16));


	       setcolor(12);
	       outtextxy(_x-50,cY,">>");

	    do{
				key=getch();


			  if(key==UP)
			  {
				setcolor(0);
				outtextxy(_x-50,cY,">>");

				cY-=_h;
				choice--;

				if(choice<1)
				{
					choice=11;
					cY =_y+12*_h;
				}

				setcolor(12);
				outtextxy(_x-50,cY,">>");
				sound(1000);
				delay(20);
				nosound();

			  }
			  else if(key==DOWN)
			  {
				setcolor(0);
				outtextxy(_x-50,cY,">>");
				cY+=_h;
				choice++;
				if(choice>11)
				{
					choice=1;
					cY=_y+2*_h;
				}

				setcolor(12);
				outtextxy(_x-50,cY,">>");
				sound(1000);
				delay(20);
				nosound();
			 }

		}while(key!=13);

			switch(choice)
			{
				case 1:
				SPEED=500;
				level=1;
				choice=0;
				break;
				case 2:
				SPEED=450;
				level=2;
				choice=0;
				break;
				case 3:
				SPEED=400;
				level=3;
				choice=0;
				break;
				case 4:
				SPEED=350;
				level=4;
				choice=0;
				break;
				case 5:
				SPEED=300;
				level=5;
				choice=0;
				break;
				case 6:
				SPEED=250;
				level=6;
				choice=0;
				break;
				case 7:
				SPEED=200;
				level=7;
				choice=0;
				break;
				case 8:
				SPEED=150;
				level=8;
				choice=0;
				break;
				case 9:
				SPEED=100;
				level=9;
				choice=0;
				break;
				case 10:
				SPEED=50;
				level=10;
				choice=0;
				break;
				case 11:
				closegraph();
				restorecrtmode();
				clrscr();
				cout<<"\n\n\t\t Thank You for playing Tetris Game.";
				cout<<"\n\n\tPlease visit our hompage : www.justdocodings.blogspot.in\n\n\n";
				exit(0);
				break;

			}

	}while(choice!=0);

	cleardevice();
}

//***************************************************************
//   Function to reset Game
//****************************************************************

void resetGame()
{
	for(int i=0;i<Th;i++)
		for(int j=0;j<Tl;j++)
		{
			Tetris[i][j]=0;
			temp[i][j]=0;
			colorInfo[i][j]=0;
			tempColorInfo[i][j]=0;

		}
	for(int k=0;k<4;k++)
	{
		start_x[k]=0;
		start_y[k]=0;
		prev_x[k]=0;
		prev_y[k]=0;
	}
	whichDesign=NONE;
	designColor=0;
	nextDesign=NONE;
	Turn=1;
	clockAnti = NOTMOVE;
	score=0;
	level=1;
	lines=0;

	nextFlag=0;
	resetSpeed=FALSE;
	disableSound=FALSE;


}

//***************************************************************
//   Function to check if game is over or not 
//****************************************************************

void GameOver(int check)
{



	for(int i=0;i<Tl;i++)
		if(Tetris[2][i]==TRUE)
		{
			isGameOver=TRUE;
			break;
		}
	if(isGameOver==TRUE || check==0)
	{
		cleardevice();





		settextstyle(0,0,7);
		Text3D(100,150,4,3,11,"Game Over");
		settextstyle(0,0,4);
		Text3D(180,300,2,3,11,"Score : ");
		Text3D(180+textwidth("Score : "),300,2,3,11,itoa(score,buffer,10));
		settextstyle(0,0,2);
		Text3D(100,400,2,3,11,"Press any key to continue...");
		settextstyle(0,0,0);
		for(int j=0;j<2000;j++)
			putpixel(random(640),random(480),random(16));

		getch();
		resetGame();
		mainMenu();

		InitBackground();
		randomize();
		whichDesign=random(8);
		if(whichDesign==0)
			whichDesign=3;

		nextDesign=random(8);
		if(nextDesign==0)
			nextDesign=3;

		InitDesign();
		Draw();

		nextFlag=TRUE;
		drawNextPattern(X+(Tl*W)-W,Y-1+H);


	}


}

//*********************************************************************
//   Function to draw black border for each square of a pattern
//*********************************************************************

void redrawPatternBorder()
{
	for(int r_y=0;r_y<Th;r_y++)
		for(int r_x=0;r_x<Tl;r_x++)
		{
			if(Tetris[r_y][r_x]==1)
			{
				setcolor(0);	
				rectangle(X+(r_x*W),Y+(r_y*H),X+(r_x*W)+W,Y+(r_y*H)+H);
			}	
						
		}
}


//***************************************************************
//   MAIN FUNCTION
//****************************************************************

void main()
{
	int gd=DETECT,gm;
	int key=0;


	initgraph(&gd,&gm,"c://turboc3//bgi");


	Start();
	Intro();
	mainMenu();
	InitBackground();


	randomize();
	whichDesign=random(8);
	if(whichDesign==0)
		whichDesign=3;

	nextDesign=random(8);
	if(nextDesign==0)
		nextDesign=3;

	InitDesign();
	Draw();

	nextFlag=TRUE;
	drawNextPattern(X+(Tl*W)-W,Y-1+H);

	while(1)
	{




		if(check_y(Th-1)==FALSE && checkCollision(MOVEDOWN)==FALSE)
		{
			if(nextFlag==FALSE)
			{

				nextDesign=random(8);
				if(nextDesign==0)
					nextDesign=3;

				nextFlag=TRUE;

				updateData();

				drawNextPattern(X+(Tl*W)-W,Y-1+H);


			}

			moveDown();
			redrawPatternBorder();
			
				
			if(resetSpeed==FALSE)
			delay(SPEED);
			else
			{
				resetSpeed=FALSE;
				if(level==9||level==10)
				delay(SPEED-40);
				else
				delay(SPEED-80);
			}
			if(disableSound==FALSE)
			{	
				sound(700);
				delay(30);
				nosound();
			}	


		}
		else
		{
			lineCompleted();
			lineCompleted();
			isGameOver=FALSE;
			GameOver(1);
			
            if(isGameOver==FALSE)
			{				
				if(nextFlag==TRUE)
				whichDesign=nextDesign;
				InitDesign();
				Draw();
			}
			
			Turn=1;

			nextFlag=FALSE;

		}


		while(kbhit())
		{
			key=getch();

			switch(key)
			{
				case LEFT:
				if(check_x(0)==FALSE && checkCollision(MOVELEFT)==FALSE )
				{
					moveLeft();
					redrawPatternBorder();
					delay(SPEED);
					if(disableSound==FALSE)
					{	
						sound(700);
						delay(30);
						nosound();
					}	
				}
				break;
				case RIGHT:
				if(check_x(Tl-1)==FALSE && checkCollision(MOVERIGHT)==FALSE )
				{
					moveRight();
					redrawPatternBorder();
					delay(SPEED);
					if(disableSound==FALSE)
					{	
						sound(700);
						delay(30);
						nosound();
					}	
				}
				break;
				case UP:
				rotateShapes();
				break;
				case DOWN:
					resetSpeed=TRUE;
				break;
				case SPACE:
					getch();
				break;
				case EXIT:
					isGameOver=FALSE;
					GameOver(0);
				case 'S':
				case 's':
					if(disableSound==FALSE)
						disableSound=TRUE;
					else
						disableSound=FALSE;
				break;

			}

		}
	}


}
