OUT = /mnt/c/Users/claud/Downloads/
scale=100

test: c b
	./skeletal.py tests/modelDetails.json tests/modesPostG.yaml -o /mnt/c/Users/claud/Downloads/hayward-skeletal.html \
		--vert 3 --scale 800 # --show origin

basics:
	@./skeletal.py --version | grep '^[0-9]*\.[0-9]*\.[0-9]*$$' > /dev/null && echo "Pass"
c:
	./skeletal.py --show origin --vert 2 -s $(scale) -o $(OUT)/painter-2.html tests/c.json -d 5:tran # -d 5:plan
	./skeletal.py --show origin --vert 2 -s $(scale) -o $(OUT)/painter-2.json tests/c.json -d 5:tran # -d 5:plan
	./skeletal.py --show origin --vert 2 -s $(scale) -o $(OUT)/painter-2-elev.html tests/c.json -d 2:elev -d 5:elev
	./skeletal.py --show origin --vert 2 -s $(scale) -o $(OUT)/painter-2-tran.html tests/c.json -d 2:tran -d 5:tran
	./skeletal.py --show origin --vert 2 -s $(scale) -o $(OUT)/painter-2-long.html tests/c.json -d 2:long -d 5:long
	./skeletal.py --show origin --vert 2 -s $(scale) -o $(OUT)/painter-2-full.html tests/c.json \
		-d 2:long -d 5:long -d 2:vert -d 5:vert -d 2:elev -d 5:elev

b:
	./skeletal.py -s $(scale) -o $(OUT)/painter-3.html tests/b.json --vert 3 -d 5:tran # -d 5:plan
	./skeletal.py -s $(scale) -o $(OUT)/painter-3.json tests/b.json --vert 3 -d 5:tran # -d 5:plan
	./skeletal.py --show origin --vert 3 -s $(scale) -o $(OUT)/painter-3-elev.html tests/b.json -d 2:elev -d 5:elev
	./skeletal.py --show origin --vert 3 -s $(scale) -o $(OUT)/painter-3-tran.html tests/b.json -d 2:tran -d 5:tran
	./skeletal.py --show origin --vert 3 -s $(scale) -o $(OUT)/painter-3-long.html tests/b.json -d 2:long -d 5:long
	./skeletal.py --show origin --vert 3 -s $(scale) -o $(OUT)/painter-3-full.html tests/c.json \
		-d 2:long -d 5:long -d 2:vert -d 5:vert -d 2:elev -d 5:elev

