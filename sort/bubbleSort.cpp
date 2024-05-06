#include<iostream>
using namespace std;
void swap(int array[],int i,int j){
    int temp=array[i];
    array[i]=array[j];
    array[j]=temp;
}

void BubbleSort(int array[],int n)
{
    for (int i=0;i<n-1;i++)
    {
        for (int j=i+1;j<n-1;j++)
        {
            if (array[i]>array[j])
            {
                swap(array,i,j);
            }
        }
    }
}