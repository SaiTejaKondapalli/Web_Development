function deepEqual(a, b) {

	if (typeof a === 'object' && typeof b === 'object') {

		let count = 0
		const aKeys = Object.keys(a)
		const bKeys = Object.keys(b)

		for (let i = 0; i < aKeys.length; i++) {

			for (let j = 0; j < bKeys.length; j++) {

				if (deepEqual(a[aKeys[i]], b[bKeys[j]])) {
					count++
					break
				}

			}
		}
		if (count === aKeys.length && count === bKeys.length)
			return true
		else
			return false
	}
	else
		return a === b
}

const one = {
	1:'hello',
	2:'world',
}

const two = {
	1:'hello',
	2:'world',
}

const three = {
	1:'hello',
	2:'world',
	inner: {
		key:"value"
	},
}

const four = {
	1:'hello',
	2:'world',
	inner: {
		key:"value"
	},
}

const obj = {
	here: {
		is: "an"
	},
	object: 2
}

console.log(deepEqual(5, 5))
console.log(deepEqual(one, one))
console.log(deepEqual(one, three))
console.log(deepEqual(three, four))
console.log(deepEqual(obj, obj))
console.log(deepEqual(obj,{object: 2, here: {is: "an"}}))