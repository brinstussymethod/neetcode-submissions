class TimeMap {
public:
    map<string, map<int, string>> timeStamp;

    TimeMap() {
        
    }
    
    void set(string key, string value, int timestamp) {
        this->timeStamp[key][timestamp] = value; 
    }
    
    string get(string key, int timestamp) {
        if (timeStamp.find(key) == timeStamp.end()) {
            return "";
        }

        auto& innerMap = timeStamp[key];

        auto it = innerMap.upper_bound(timestamp);

        if (it == innerMap.begin()) {
            return "";
        }

        it--;
        return it->second;
    }
};
