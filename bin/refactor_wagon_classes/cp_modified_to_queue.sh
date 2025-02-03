mkdir -p ./tmp/insertion_queue
for file in ./tmp/modified_consist_classes/*.py; do
    base=$(basename "$file")
    if ! diff -q --strip-trailing-cr "$file" "./tmp/consist_classes/$base" >/dev/null; then
        cp "$file" "./tmp/insertion_queue/"
    fi
done
