class Solution {
   public:
    int maxDepth(TreeNode* root) {
        queue<TreeNode*> queue;
        if (root != nullptr) queue.push(root);

        int level = 0;
        while (!queue.empty()) {
            int size = queue.size();

            for (int i = 0; i < size; i++) {
                TreeNode* node = queue.front();
                queue.pop();

                if (node->left != nullptr) {
                    queue.push(node->left);
                }

                if (node->right != nullptr) {
                    queue.push(node->right);
                }
            }

            level++; 
        }

        return level; 
    }
};