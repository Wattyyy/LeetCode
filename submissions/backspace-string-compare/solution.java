class Solution {
    public LinkedList<Character> processString(String s) {
        LinkedList<Character> list = new LinkedList();
        for (int i = 0; i < s.length(); i++) {
            if (s.charAt(i) != '#') {
                list.addLast(s.charAt(i));
            }
            else {
                if (list.size() > 0) {
                    list.removeLast();
                }
            }
        }
        return list;
    }
    public boolean backspaceCompare(String s, String t) {
        LinkedList<Character> l1 = processString(s);
        LinkedList<Character> l2 = processString(t);
        if (l1.size() != l2.size()) {
            return false;
        }
        for (int i = 0; i < l1.size(); i++) {
            if (l1.get(i) != l2.get(i)) {
                return false;
            }
        }
        return true;
    }
}
