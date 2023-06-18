#include <bits/stdc++.h>
using namespace std;

int main() {
    int no_of_sites, no_of_critical_sites, timestamp_of_critical_site, critical_site;
    cout << "Enter number of sites : ";
    cin >> no_of_sites;
    cout << "Enter number of sites which want to enter critical section: ";
    cin >> no_of_critical_sites;

    vector<int> timestamp_vctr(no_of_sites, 0);
    vector<int> request_vctr;
    map<int, int> mp;

    for (int i = 0; i < no_of_critical_sites; i++) {
        cout << "\nEnter timestamp: ";
        cin >> timestamp_of_critical_site;
        cout << "Enter critical_site number: ";
        cin >> critical_site;
        timestamp_vctr[critical_site - 1] = timestamp_of_critical_site;
        request_vctr.push_back(critical_site);
        mp[timestamp_of_critical_site] = critical_site;
    }

    cout << "\nSites and Timestamp: \n";
    for (int i = 0; i < timestamp_vctr.size(); i++) {
        cout << i + 1 << " " << timestamp_vctr[i] << endl;
    }

    for (int i = 0; i < request_vctr.size(); i++) {
        cout << "\n Request from critical_site: " << request_vctr[i] << endl;
        for (int j = 0; j < timestamp_vctr.size(); j++) {
            if (request_vctr[i] != (j + 1)) {
                if (timestamp_vctr[j] > timestamp_vctr[request_vctr[i] - 1] || timestamp_vctr[j] == 0)
                    cout << j + 1 << " Replied\n";
                else
                    cout << j + 1 << " Deferred\n";
            }
        }
    }
    cout << endl;

    map<int, int>::iterator it;
    it = mp.begin();
    for (it = mp.begin(); it != mp.end(); it++) {
        cout << "Site " << it->second << " entered Critical Section \n";
    }
    return 0;
}