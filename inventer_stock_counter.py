product_batches = [135, 72, 45, 210]
box_capacity = 50
packed_inventory = []

batch_index = 0
while batch_index < len(product_batches):
    loose_items = product_batches[batch_index]
    boxes_in_batch = 0
    
    while loose_items >= box_capacity:
        boxes_in_batch += 1
        loose_items -= box_capacity
        
    packed_inventory.append({
        "batch_id": batch_index + 1, 
        "boxes": boxes_in_batch, 
        "leftover": loose_items
    })
    batch_index += 1

print("=" * 45)
print("FINAL INVENTORY STOCK REPORT")
print("=" * 45)

for batch in packed_inventory:
    print(f"\nBatch {batch['batch_id']}:")
    print(f"  > Total Boxes Packed ({box_capacity} items each): {batch['boxes']}")
    print(f"  > Loose Items Remaining: {batch['leftover']}")
    
    if batch['leftover'] > 0:
        print("  > Item Details:")
        for item_num in range(1, batch['leftover'] + 1):
            print(f"    - Serial Unit: {batch['batch_id']}-L{item_num}")

print("\n" + "=" * 45)
print("End of Report")