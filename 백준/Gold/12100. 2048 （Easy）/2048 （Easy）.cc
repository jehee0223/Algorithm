#include<iostream>
using namespace std;

int n, rtn;
int map[20][20];
bool combine[20];

void BT(int m[20][20], int cnt) {

    if (cnt == 5) {
        int Max = 0;
        for (int i = 0; i < n; i++)
            for (int j = 0; j < n; j++)
                Max = Max > m[i][j] ? Max : m[i][j];

        rtn = rtn > Max ? rtn : Max;
        //Print(m);
        return;
    }

    int tmap[20][20];

    for (int x = 0; x < 4; x++)
    {
        for (int i = 0; i < n; i++)
            for (int j = 0; j < n; j++)
                tmap[i][j] = m[i][j];

        if (x == 0)
        { //상 
            for (int i = 0; i < n; i++) //열  
            {
                for (int j = 1; j < n; j++) //행  
                {
                    if (tmap[j][i] == 0) continue;

                    for (int k = j - 1; k >= 0; k--)
                    {

                        if ((tmap[k + 1][i] == tmap[k][i]) && !combine[k])// Combine
                        {
                            tmap[k][i] *= 2;
                            combine[k] = true;
                            tmap[k + 1][i] = 0;
                            break;
                        }
                        else if (tmap[k][i] == 0) //Swap
                        {

                            tmap[k][i] = tmap[k + 1][i];
                            tmap[k + 1][i] = 0;
                        }
                        else break; 
                    }

                }
                for (int k = 0; k < n; k++)
                    combine[k] = false;
            }
        }
        //하  
        else if (x == 1)
        {
            for (int i = 0; i < n; i++) 
            {
                for (int j = n - 2; j >= 0; j--) 
                {
                    if (tmap[j][i] == 0) continue;

                    for (int k = j + 1; k < n; k++)
                    {

                        if ((tmap[k - 1][i] == tmap[k][i]) && !combine[k]) 
                        {
                            tmap[k][i] *= 2;
                            combine[k] = true;
                            tmap[k - 1][i] = 0;
                            break;
                        }
                        else if (tmap[k][i] == 0)
                        {

                            tmap[k][i] = tmap[k - 1][i];
                            tmap[k - 1][i] = 0;
                        }
                        else break;
                    }

                }
                for (int k = 0; k < n; k++)
                    combine[k] = false;
            }
        }
        //좌  
        else if (x == 2)
        {
            for (int i = 0; i < n; i++) 
            {
                for (int j = 1; j < n; j++)   
                {
                    if (tmap[i][j] == 0) continue;

                    for (int k = j - 1; k >= 0; k--)
                    {

                        if ((tmap[i][k + 1] == tmap[i][k]) && !combine[k])
                        {
                            tmap[i][k] *= 2;
                            combine[k] = true;
                            tmap[i][k + 1] = 0;
                            break;
                        }
                        else if (tmap[i][k] == 0)
                        {

                            tmap[i][k] = tmap[i][k + 1];
                            tmap[i][k + 1] = 0;
                        }
                        else break;
                    }

                }
                for (int k = 0; k < n; k++)
                    combine[k] = false;
            }
        }
        else
        {
            for (int i = 0; i < n; i++)
            {
                for (int j = n - 2; j >= 0; j--)
                {
                    if (tmap[i][j] == 0) continue;

                    for (int k = j + 1; k < n; k++)
                    {

                        if ((tmap[i][k - 1] == tmap[i][k]) && !combine[k])
                        {
                            tmap[i][k] *= 2;
                            combine[k] = true;
                            tmap[i][k - 1] = 0;
                            break;
                        }
                        else if (tmap[i][k] == 0)
                        {

                            tmap[i][k] = tmap[i][k - 1];
                            tmap[i][k - 1] = 0;
                        }
                        else break;
                    }

                }
                for (int k = 0; k < n; k++)
                    combine[k] = false;
            }
        }
        BT(tmap, cnt + 1);
    }

}

int main() {
    cin >> n;

    for (int i = 0; i < n; i++)
        for (int j = 0; j < n; j++)
            cin >> map[i][j];

    BT(map, 0);

    cout << rtn;

}