.PHONY: test clean
RUST_DIR=rust
RUST_BUILD_DIR=$(RUST_DIR)/build
TARGET=$(subst .rs,,$(subst $(RUST_DIR),$(RUST_BUILD_DIR),$(wildcard $(RUST_DIR)/*.rs)))
all: $(TARGET)

$(RUST_BUILD_DIR):
	mkdir -p $@

$(RUST_BUILD_DIR)/%:$(RUST_DIR)/%.rs $(RUST_BUILD_DIR)
	rustc $< -o $@

clean:
	rm -rf $(RUST_BUILD_DIR)

test: all
	echo "Testing Rust katas"
	for e in $(RUST_BUILD_DIR)/*; do echo "$$e"; "$$e"; done

	echo "Testing Python katas"
	env PYTHONHASHSEED=0 PYTHONPATH=python/ python3 -m doctest python/*.py
	env PYTHONPATH=python/euler python3 -m doctest python/*/*.py
