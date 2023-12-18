/**
 * This file was auto-generated by Fern from our API Definition.
 */
package com.seed.unknownAsAny;

import com.seed.unknownAsAny.core.ClientOptions;
import com.seed.unknownAsAny.core.Suppliers;
import com.seed.unknownAsAny.unknown._UnknownClient;
import java.util.function.Supplier;

public class UnknownAsAny {
    protected final ClientOptions clientOptions;

    protected final Supplier<_UnknownClient> unknownClient;

    public UnknownAsAny(ClientOptions clientOptions) {
        this.clientOptions = clientOptions;
        this.unknownClient = Suppliers.memoize(() -> new _UnknownClient(clientOptions));
    }

    public _UnknownClient unknown() {
        return this.unknownClient.get();
    }

    public static UnknownAsAnyBuilder builder() {
        return new UnknownAsAnyBuilder();
    }
}
