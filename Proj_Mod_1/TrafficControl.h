//
//  TrafficControl.h
//  Proj_Mod_1
//
//  Created by vaibhav sethia on 10/06/19.
//  Copyright © 2019 vaibhav sethia. All rights reserved.
//

#ifndef TrafficControl_h
#define TrafficControl_h

#include "Light.h"
#include "Time.h"
#include <curses.h>
#include <algorithm>
#include "Input.h"
#include "Calci.h"

using namespace std;

void NormalLights(vector<pair<int,int>> &NoC, int Num )
{
    int Gtime=30;
    int TimeCount=1;
    for(int i=0;i<Num;i++)
    {
        for(int j=0;j<Gtime;j++)
        {
            clear();
            Delay(1);
            TimeCount++;
            cout<<TimeCount<<endl;
            GreenLight(NoC[i].second);
        }
        YellowLight(NoC[i].second);
        Delay(4);
        TimeCount +=4;
        RedLight();
        TimeCount++;
    }
}


void CongestionLights(vector<pair<int,int>> &NoC, int Norm, int Num)
{
    int TimeCount=1;
    if(NoC[Num-1].first<10)
    {
        for(int j=0;j<15;j++)
        {
            clear();
            Delay(1);
            TimeCount++;
            cout<<TimeCount<<endl;
            GreenLight(NoC[Num-1].second);
            NoC[Num-1].first=0;
        }
        YellowLight(NoC[Num].second);
        Delay(4);
        TimeCount +=4;
        RedLight();
        TimeCount++;
    }
    
    while(NoC[0].first!=0)
    {
        int Gtime=Interval(NoC, Num);
        int PassableCars=Gtime*2/3;
        for(int j=0;j<Gtime;j++)
        {
            clear();
            Delay(1);
            TimeCount++;
            cout<<TimeCount<<endl;
            GreenLight(NoC[0].second);
            NoC[0].first-=PassableCars;
            if(NoC[0].first<0)
                NoC[0].first=0;
        }
        sort(NoC.begin(), NoC.end(), comparator);
    }
}

#endif /* TrafficControl_h */
