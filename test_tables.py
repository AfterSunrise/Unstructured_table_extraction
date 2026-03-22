from unstructured.partition.pdf import partition_pdf

pdf_path = "kb_ai.pdf"

elements = partition_pdf(
    filename=pdf_path,
    strategy="hi_res",
    languages=["eng", "kor"],
    coordinates=True,
    unique_element_ids=True,
    skip_infer_table_types=[],
)

print(f"Total elements detected: {len(elements)}")

tables = [el for el in elements if el.category == "Table"]
print(f"Total tables detected: {len(tables)}")

for i, table in enumerate(tables, start=1):
    print("\n" + "=" * 80)
    print(f"[Table {i}]")
    print(f"id: {getattr(table, 'id', None)}")
    print(f"page_number: {getattr(table.metadata, 'page_number', None)}")

    coords = getattr(table.metadata, "coordinates", None)
    print(f"coordinates: {coords}")

    print("\n--- metadata ---")
    print(vars(table.metadata))

    print("\n--- table text preview ---\n")
    print((table.text or "")[:1500])

    html = getattr(table.metadata, "text_as_html", None)
    if html:
        html_name = f"table_{i}.html"
        with open(html_name, "w", encoding="utf-8") as f:
            f.write(html)
        print(f"\nSaved HTML table -> {html_name}")
    else:
        print("\nNo HTML structure detected")

for idx, el in enumerate(elements):
    if el.category == "Table":
        print("\n" + "=" * 100)
        print(f"TABLE INDEX IN ELEMENTS: {idx}")
        print(f"TABLE ID: {getattr(el, 'id', None)}")
        print(f"TABLE PAGE: {getattr(el.metadata, 'page_number', None)}")

        start = max(0, idx - 5)
        end = min(len(elements), idx + 6)

        for j in range(start, end):
            e = elements[j]
            print(
                f"\n[{j}] id={getattr(e, 'id', None)} "
                f"category={e.category} "
                f"page={getattr(e.metadata, 'page_number', None)}"
            )
            print((e.text or "")[:300])