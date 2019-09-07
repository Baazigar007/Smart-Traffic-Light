//
//  main.cpp
//  Proj_Mod_1
//
//  Created by vaibhav sethia on 09/06/19.
//  Copyright © 2019 vaibhav sethia. All rights reserved.
//

#include <iostream>
#include "Input.h"
#include "Dummies.h"
#include <algorithm>
#include "Time.h"
#include "TrafficControl.h"

//Assuming that 20 cars can cross the intersection in 30 seconds


int main(int argc, const char * argv[]) {
    int NormVal=20;
    vector<pair<int,int>> NumberOfCars;
    cout<<"CHECK";
    GetInput(NumberOfCars);
    PrintPairVal(NumberOfCars, 0);
    sort(NumberOfCars.begin(),NumberOfCars.end(),comparator);
    PrintVec(NumberOfCars, 4);
    if(GetPairVal(NumberOfCars, 4) <=NormVal)
        NormalLights(NumberOfCars,4);
    else
        CongestionLights(NumberOfCars,20 , 4);
    return 0;
}
