class Solution {
   public:
    int maxDepth(TreeNode* root) {
        int counter = 0;

        helper(root, 1, &counter);
        return counter; 
    }

    void helper(TreeNode* node, int currentDepth, int* counter) {
        if (!node) return;

        if (currentDepth > *counter) *counter = currentDepth;

        helper(node->left, currentDepth + 1, counter);
        helper(node->right, currentDepth + 1, counter);
    }
};