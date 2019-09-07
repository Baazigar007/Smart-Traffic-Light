//
//  Input.h
//  Proj_Mod_1
//
//  Created by vaibhav sethia on 09/06/19.
//  Copyright © 2019 vaibhav sethia. All rights reserved.
//

#ifndef Input_h
#define Input_h
#include <vector>

using namespace std;

void GetInput(vector<pair<int,int>> &NoC)
{
    int num=0;
    for(int i=0;i<4;i++)
    {
        cin>>num;
        NoC.push_back(make_pair(num,i));
    }
}

bool comparator(const pair<int,int> A , const pair<int,int> B)
{
    return A.first>B.first;
}

#endif /* Input_h */
