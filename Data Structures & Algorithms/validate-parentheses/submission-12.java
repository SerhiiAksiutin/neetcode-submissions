class Solution {
    public boolean isValid(String s) {
        Stack<Character> stack = new Stack<>();
        Map<Character, Character> map = new HashMap<>();
        map.put(')', '(');
        map.put('}', '{');
        map.put(']', '[');

        for (char c : s.toCharArray()) {
            if (map.values().contains(c)) {
                stack.push(c);
            } else if (map.keySet().contains(c)) {
                if (stack.isEmpty()) {
                    return false;
                }
                char top = stack.pop();
                if (top != map.get(c)) {
                    return false;
                }
            }
        }

        return stack.isEmpty();
    }
}
