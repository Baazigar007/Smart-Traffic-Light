//
//  Dummies.h
//  Proj_Mod_1
//
//  Created by vaibhav sethia on 09/06/19.
//  Copyright © 2019 vaibhav sethia. All rights reserved.
//

#ifndef Dummies_h
#define Dummies_h

void PrintPairVal(vector<pair<int,int>> NoC,int Num)
{
    cout<<NoC[Num].first;
}

int GetPairVal(vector<pair<int,int>> NoC,int Num)
{
    return NoC[Num].first;
}

void PrintVec(vector<pair<int,int>> NoC,int Num)
{
    for(int i=0;i<Num;i++)
    {
        cout<<NoC[i].first<<" "<<NoC[i].second<<endl;
    }
}
#endif /* Dummies_h */
