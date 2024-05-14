/**
 * This file was auto-generated by Fern from our API Definition.
 */

import * as serializers from "../../../index";
import * as SeedExamples from "../../../../api/index";
import * as core from "../../../../core";
import { Type } from "../../../types/Type";

export const ResponseType: core.serialization.ObjectSchema<serializers.ResponseType.Raw, SeedExamples.ResponseType> =
    core.serialization.object({
        type: Type,
    });

export declare namespace ResponseType {
    interface Raw {
        type: Type.Raw;
    }
}