//
//  Calci.h
//  Proj_Mod_1
//
//  Created by vaibhav sethia on 09/06/19.
//  Copyright © 2019 vaibhav sethia. All rights reserved.
//

#ifndef Calci_h
#define Calci_h
#include<math.h>

int Round(int n)
{
    int a = (n / 10) * 10;
    int b = a + 10;
    return (n - a > b - n)? b : a;
}

int Mean(vector<pair<int,int>> NoC,int Num)
{
    int sum=0;
    for (int i=0; i<Num; i++) {
        sum += NoC[i].first;
    }
    return sum/Num;
}

int Variance(vector<pair<int,int>> NoC,int Num)
{
    int sum=0;
    int mean=Mean(NoC,Num);
    for (int i = 0; i < Num; i++)
    {
        sum = sum + pow((NoC[i].first - mean), 2);
    }
    return sum/Num;
}

int STDev(vector<pair<int,int>> NoC,int Num)
{
    return sqrt(Variance(NoC,Num));
}

#endif /* Calci_h */
