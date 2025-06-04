original_list = [1,2,3,4,5,6,7,8,9,10]
print("Original list: ",original_list)

extracted_list = original_list[0:5]
print(f"Extracted first five elements: ",extracted_list)

reversed_list = extracted_list[:]
reversed_list.reverse()
print(f"Reversed extracted elements: ",reversed_list)