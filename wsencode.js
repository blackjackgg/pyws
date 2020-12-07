
//第一步  转化unit8  11311
rawbyte =""
_writeUint8Array(new Uint8Array(rawbyte))



        r.prototype.readBytes = function(e, r, i) {
            return void 0 === r && (r = 0),
            void 0 === i && (i = 0),
            this._readByte ? (this._readByte.position = 0,
            this._readByte.readBytes(e, r, i),
            void this._readByte.clear()) : void t.$warn(3102)
        }

function _writeUint8Array(t, e) {
            void 0 === e && (e = !0);
            var i = this._position
              , r = i + t.length;
            e && this.validateBuffer(r),
            this.bytes.set(t, i),
            this.position = r
        }