// The basic solution, where getProduct() is O(k).
class ProductOfNumbers {
private:
    std::vector<int> stream;

public:
    ProductOfNumbers() {
    }
    
    void add(int num) {
        stream.push_back(num);
    }
    
    int getProduct(int k) {
        int result = 1;
        int size = stream.size();

        for (int i = size - k; i < size; ++i) {
            result *= stream[i];
        }

        return result;
    }
};

/**
 * Your ProductOfNumbers object will be instantiated and called as such:
 * ProductOfNumbers* obj = new ProductOfNumbers();
 * obj->add(num);
 * int param_2 = obj->getProduct(k);
 */
