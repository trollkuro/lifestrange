

window.Modal = (function () {
	var Modal = function (template) {
		this._element = document.createElement('div');
		this._element.className += ' such-modal';
		console.log(template);
		this._element.innerHTML = template;
		this._content = this._element.children[0];

		this._element.addEventListener('click', function (event) {
			if(event.target === this) {
				this.style.display = 'none';
			}
		})
	}

	Object.assign(Modal.prototype, {
		open: function () {
			console.log('test');
			this._element.style.display = 'block';
		},
		close: function () {
			this._element.style.display = 'none';
		}
	});

	return Modal;
})();


window.SuchDialog = (function () {
	var noop = function (argument) {};
	var defaultOptions = {
		template: '',
		beforeShow: noop,
		onReady: noop
	};
	var modal = null;

	return {
		open: open
	};

	function open(options) {
		options = Object.assign({}, defaultOptions, options);

		if(!modal) { 
			modal = new Modal(options.template);
			document.body.appendChild(modal._element); 
		}

		options.beforeShow(modal._content, modal);
		modal.open();
		options.onReady(modal._content, modal);
	}
})();