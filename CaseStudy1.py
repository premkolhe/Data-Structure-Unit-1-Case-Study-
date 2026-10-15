from dataclasses import dataclass


# ---------- Part 1: E-commerce product sorting ----------
@dataclass
class Product:
    name: str
    price: float
    rating: float


def merge_sort(products, key):
    """Return products sorted by key using the Merge Sort algorithm."""
    if len(products) <= 1:
        return products

    middle = len(products) // 2
    left = merge_sort(products[:middle], key)
    right = merge_sort(products[middle:], key)

    return merge(left, right, key)


def merge(left, right, key):
    """Merge two already-sorted product lists."""
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        # <= keeps the sort stable when values are equal.
        if key(left[i]) <= key(right[j]):
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result


def display_products(products):
    print(f"{'Product':<18} {'Price':>10} {'Rating':>10}")
    print("-" * 42)
    for product in products:
        print(f"{product.name:<18} ${product.price:>9.2f} {product.rating:>9.1f}")


# ---------- Part 2: Calendar event scheduling ----------
@dataclass
class Event:
    name: str
    start: int  # Time in 24-hour HHMM format, e.g. 930 means 9:30 AM
    end: int


def select_events(events):
    """
    Select the largest number of non-overlapping events.

    Greedy rule: sort by finish time, then choose the next event
    that starts at or after the last selected event's finish time.
    """
    events_by_finish = sorted(events, key=lambda event: event.end)
    selected = []
    last_finish = -1

    for event in events_by_finish:
        if event.start >= last_finish:
            selected.append(event)
            last_finish = event.end

    return selected


def format_time(time):
    hour = time // 100
    minute = time % 100
    suffix = "AM" if hour < 12 else "PM"
    display_hour = hour % 12 or 12
    return f"{display_hour}:{minute:02d} {suffix}"


def display_events(events):
    print(f"{'Event':<18} {'Start':>10} {'End':>10}")
    print("-" * 40)
    for event in events:
        print(
            f"{event.name:<18} "
            f"{format_time(event.start):>10} "
            f"{format_time(event.end):>10}"
        )


def main():
    products = [
        Product("Headphones", 799.00, 4.5),
        Product("Keyboard", 299.00, 4.2),
        Product("Smartwatch", 999.00, 4.7),
        Product("Mouse", 499.00, 4.1),
    ]

    print("PRODUCTS SORTED BY PRICE (LOW TO HIGH)")
    sorted_products = merge_sort(products, key=lambda product: product.price)
    display_products(sorted_products)

    events = [
        Event("Team Meeting", 900, 1000),
        Event("Project Review", 930, 1100),
        Event("Client Call", 1000, 1100),
        Event("Lunch Meeting", 1100, 1200),
        Event("Planning Session", 1200, 1300),
    ]

    print("\nMAXIMUM NON-OVERLAPPING CALENDAR SCHEDULE")
    selected_events = select_events(events)
    display_events(selected_events)


if __name__ == "__main__":
    main()