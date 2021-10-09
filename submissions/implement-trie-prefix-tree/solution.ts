class TrieNode {
  children: Map<string, TrieNode>;
  isword: boolean;

  constructor() {
    this.children = new Map();
    this.isword = false;
  }
}

class Trie {
  root: TrieNode;

  constructor() {
    this.root = new TrieNode();
  }

  insert(word: string): void {
    let cur: TrieNode = this.root;
    for (let i = 0; i < word.length; i++) {
      if (!cur.children.has(word[i])) {
        cur.children.set(word[i], new TrieNode());
      }
      cur = cur.children.get(word[i])!;
    }
    cur.isword = true;
  }

  search(word: string): boolean {
    let cur = this.root;
    for (let i = 0; i < word.length; i++) {
      if (!cur.children.has(word[i])) {
        return false;
      }
      cur = cur.children.get(word[i])!;
    }
    return cur.isword;
  }

  startsWith(prefix: string): boolean {
    let cur = this.root;
    for (let i = 0; i < prefix.length; i++) {
      if (!cur.children.has(prefix[i])) {
        return false;
      }
      cur = cur.children.get(prefix[i])!;
    }
    return true;
  }
}
