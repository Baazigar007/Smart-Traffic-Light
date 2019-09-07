//
//  Time.h
//  Proj_Mod_1
//
//  Created by vaibhav sethia on 09/06/19.
//  Copyright © 2019 vaibhav sethia. All rights reserved.
//

#ifndef Time_h
#define Time_h
#include<time.h>
#include<chrono>
#include "Calci.h"

void Delay(int number_of_seconds)
{
    int milli_seconds = 1000 * number_of_seconds;
    clock_t start_time = clock();
    while (clock() < start_time + milli_seconds){;}
}

int Interval(vector<pair<int,int>> NoC,int Num)
{
    int var=Variance(NoC, Num);
    if(var<200)
        return 40;
    else if(var<400)
        return 60;
    else if (var<900)
        return 75;
    else
        return 90;
}

#endif /* Time_h */
