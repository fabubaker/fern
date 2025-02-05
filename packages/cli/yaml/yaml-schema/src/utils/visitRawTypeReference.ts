import { Literal, PrimitiveType, PrimitiveTypeV1 } from "@fern-api/ir-sdk";
import { RawPrimitiveType } from "./RawPrimitiveType";

export const FernContainerRegex = {
    MAP: /^map<\s*([^,]*)\s*,\s*(.*)\s*>$/,
    LIST: /^list<\s*(.*)\s*>$/,
    SET: /^set<\s*(.*)\s*>$/,
    OPTIONAL: /^optional<\s*(.*)\s*>$/,
    LITERAL: /^literal<\s*(?:"(.*)"|(true|false))\s*>$/
};

export interface RawTypeReferenceVisitor<R> {
    primitive: (primitive: PrimitiveType) => R;
    map: (args: { keyType: string; valueType: string }) => R;
    list: (valueType: string) => R;
    set: (valueType: string) => R;
    optional: (valueType: string) => R;
    literal: (literal: Literal) => R;
    named: (named: string) => R;
    unknown: () => R;
}

export function visitRawTypeReference<R>(type: string, visitor: RawTypeReferenceVisitor<R>): R {
    switch (type) {
        case RawPrimitiveType.integer:
            return visitor.primitive({
                v1: PrimitiveTypeV1.Integer,
                v2: undefined // TODO: Add rules for integer.
            });
        case RawPrimitiveType.double:
            return visitor.primitive({
                v1: PrimitiveTypeV1.Double,
                v2: undefined // TODO: Add rules for double.
            });
        case RawPrimitiveType.long:
            return visitor.primitive({
                v1: PrimitiveTypeV1.Long,
                v2: undefined
            });
        case RawPrimitiveType.string:
            return visitor.primitive({
                v1: PrimitiveTypeV1.String,
                v2: undefined // TODO: Add rules for string.
            });
        case RawPrimitiveType.boolean:
            return visitor.primitive({
                v1: PrimitiveTypeV1.Boolean,
                v2: undefined
            });
        case RawPrimitiveType.datetime:
            return visitor.primitive({
                v1: PrimitiveTypeV1.DateTime,
                v2: undefined
            });
        case RawPrimitiveType.date:
            return visitor.primitive({
                v1: PrimitiveTypeV1.Date,
                v2: undefined
            });
        case RawPrimitiveType.uuid:
            return visitor.primitive({
                v1: PrimitiveTypeV1.Uuid,
                v2: undefined
            });
        case RawPrimitiveType.base64:
            return visitor.primitive({
                v1: PrimitiveTypeV1.Base64,
                v2: undefined
            });
        case RawPrimitiveType.bigint:
            return visitor.primitive({
                v1: PrimitiveTypeV1.BigInteger,
                v2: undefined
            });
        case RawPrimitiveType.unknown:
            return visitor.unknown();
    }

    const mapMatch = type.match(FernContainerRegex.MAP);
    if (mapMatch?.[1] != null && mapMatch[2] != null) {
        return visitor.map({
            keyType: mapMatch[1],
            valueType: mapMatch[2]
        });
    }

    const listMatch = type.match(FernContainerRegex.LIST);
    if (listMatch?.[1] != null) {
        return visitor.list(listMatch[1]);
    }

    const setMatch = type.match(FernContainerRegex.SET);
    if (setMatch?.[1] != null) {
        return visitor.set(setMatch[1]);
    }

    const optionalMatch = type.match(FernContainerRegex.OPTIONAL);
    if (optionalMatch?.[1] != null) {
        return visitor.optional(optionalMatch[1]);
    }

    const literalMatch = type.match(FernContainerRegex.LITERAL);
    if (literalMatch?.[1] != null) {
        return visitor.literal(Literal.string(literalMatch[1]));
    }
    if (literalMatch?.[2] != null) {
        const group = literalMatch[2];
        switch (group) {
            case "false":
                return visitor.literal(Literal.boolean(false));
            case "true":
                return visitor.literal(Literal.boolean(true));
            default:
                throw new Error(`Unsupported literal value: ${group}`);
        }
    }

    return visitor.named(type);
}
