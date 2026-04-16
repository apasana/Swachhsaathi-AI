def decide_priority(category, priority, waste_type):
    # Knowledge-based decision
    if priority == 'High' or waste_type == 'Hazardous':
        final_priority = 'High'
    elif category == 'Overflow' and waste_type == 'Organic':
        final_priority = 'Medium'
    else:
        final_priority = 'Low'

    # Generate alert (for demo, just return priority)
    return final_priority