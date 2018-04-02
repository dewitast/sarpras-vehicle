#include <iostream>

using namespace std;

int main () {

    int array[] = {1,2,3,4,5,6,7,100,10.200}
    int minTemp;
    minTemp = array[0];

    for(int i = 1; i < array.size(); i ++) {
        if (minTemp > array[i]) {
            minTemp = array[i];
        }
    }
    
    cout << minTemp;


    return 0;
}