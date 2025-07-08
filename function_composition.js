/**
 * Take the input of one function, compute it using that function
 * Then put that outputted integer into the next function and 
 * continue to do that for all functions in the function array
 * @param {Function[]} functions
 * @return {Function}
 */
var compose = function(functions) {
    
    return function(x) {
        for (let i = functions.length-1; i >= 0; i--){
            
            x = functions[i](x)
        }

        return x
        
    }
};

/**
 * const fn = compose([x => x + 1, x => 2 * x])
 * fn(4) // 9
 */