class Solution {
    public boolean isValid(String s) {
        List<Character> stack = new ArrayList<>();
        Map<Character, Character> mapper = new HashMap<>();
        mapper.put(')', '(');
        mapper.put('}', '{');
        mapper.put(']', '[');
        List<Character> close = new ArrayList<>(mapper.keySet());
        List<Character> open = new ArrayList<>(mapper.values());

        // if (s.length() % 2 != 0) {
        //     return false;
        // }

        for (char c : s.toCharArray()) {
            if (open.contains(c)) {
                stack.add(c);
            } else if (close.contains(c)) {
                if (stack.isEmpty()) {
                    return false;
                }
                char popOpen = stack.remove(stack.size() - 1);
                if (mapper.get(c) != popOpen) {
                    return false;
                }
            }
        }

        return stack.size() == 0;
    }
}
