# spec/calculator.spec
describe Calculator do
	before(: each) do
		@calculator = Calculator.new
	end
	
	it "should respond to push()" do
		@calculator.should respond_to(:push)
	end
	
	it "should respond to add()"do
		@calculator.should respond_to(:add)
	end
end
	