# seraching

code:-
import java.util.HashMap;
import java.util.Scanner;

public class ConstantTimeSearchWithCharKeyAndStringValue {
    public static void main(String[] args) {
        // Create a HashMap
        HashMap<Character, String> hashMap = new HashMap<>();
        Scanner scanner = new Scanner(System.in);

        // Get the number of entries from the user
        System.out.print("Enter the number of entries: ");
        int numEntries = scanner.nextInt();
        scanner.nextLine(); // Consume the newline

        // Get key-value pairs from the user
        for (int i = 0; i < numEntries; i++) {
            System.out.print("Enter key (character) for entry " + (i + 1) + ": ");
            char key = scanner.nextLine().charAt(0);
            System.out.print("Enter value (string) for entry " + (i + 1) + ": ");
            String value = scanner.nextLine();
            hashMap.put(key, value);
        }

        // Ask the user for a key to search
        System.out.print("Enter the key (character) to search: ");
        char keyToSearch = scanner.nextLine().charAt(0);

        // Search for the key in constant time
        if (hashMap.containsKey(keyToSearch)) {
            System.out.println(keyToSearch + " found with value: " + hashMap.get(keyToSearch));
        } else {
            System.out.println(keyToSearch + " not found.");
        }

        scanner.close();
    }
}




explation:-

### Time Complexity:

1. **Insertion (`hashMap.put(key, value)`):**
   - Inserting a key-value pair into a `HashMap` generally has an average time complexity of **O(1)** (constant time) due to the hash function.
   - However, in the worst case (e.g., when many keys hash to the same index, leading to collisions), the time complexity can degrade to **O(n)**, where `n` is the number of entries in the `HashMap`.

2. **Search (`hashMap.containsKey(key)` and `hashMap.get(key)`):**
   - Searching for a key in a `HashMap` also has an average time complexity of **O(1)**. The hash function is used to directly locate the index of the key.
   - In the worst case, if there are many collisions, the time complexity can degrade to **O(n)**.

3. **Loop Iteration:**
   - The loop iterates `numEntries` times, so the total time complexity for filling the `HashMap` is **O(numEntries)**.

### Space Complexity:

1. **HashMap Storage:**
   - The space complexity for the `HashMap` is **O(n)**, where `n` is the number of key-value pairs. This is because the `HashMap` stores each key-value pair, which takes space proportional to the number of entries.

2. **Additional Space:**
   - The program uses some additional space for variables like `scanner` and other local variables, but this space is negligible compared to the `HashMap` storage.

### Example Analysis:

Consider the example where the user inputs 3 key-value pairs:

```
Enter the number of entries: 3
Enter key (character) for entry 1: A
Enter value (string) for entry 1: APPLE
Enter key (character) for entry 2: B
Enter value (string) for entry 2: BANANA
Enter key (character) for entry 3: C
Enter value (string) for entry 3: CHERRY
Enter the key (character) to search: B
B found with value: BANANA
```

- **Time Complexity:**
  - Inserting each pair (`A -> APPLE`, `B -> BANANA`, `C -> CHERRY`) takes O(1) time per insertion, resulting in **O(1)** per operation.
  - Searching for the key `B` takes **O(1)** time as well.

- **Space Complexity:**
  - The `HashMap` stores 3 key-value pairs, so the space complexity is **O(3)**, which is effectively **O(n)** where `n` is the number of entries.

### Summary:

- **Time Complexity:** O(1) on average for insertions and searches, O(n) in the worst case.
- **Space Complexity:** O(n) for storing key-value pairs.
