#include<iostream>
using namespace std;
void quickSort(int a[],int,int);

int main(){
    int array[]={34,65,12,43,67,5,78,10,3,70};
    int k;
    int len=sizeof(array)/sizeof(int);
    quickSort(array,0,len-1);

}

void quickSort(int array[],int left,int right){
    if (left<right)
    {
    int i=left;
    int j=right;
    int key=array[i];
    while(i<j){
        while(i<j && array[j]>=key){
            j--;
        }
        if(i<j){
            array[i]=array[j];
        }
        while(i<j&& array[i]<=key)
        {
            i++;
        }
        if (i<j){
            array[j]=array[i];
        }
    }
    array[i]=key;
    quickSort(array,left,i-1);
    quickSort(array,i+1,right);
    }

}