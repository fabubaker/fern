/**
 * This file was auto-generated by Fern from our API Definition.
 */
import * as serializers from "../../../../..";
import * as SeedTrace from "../../../../../../api";
import * as core from "../../../../../../core";
export declare const VoidFunctionDefinitionThatTakesActualResult: core.serialization.ObjectSchema<serializers.v2.VoidFunctionDefinitionThatTakesActualResult.Raw, SeedTrace.v2.VoidFunctionDefinitionThatTakesActualResult>;
export declare namespace VoidFunctionDefinitionThatTakesActualResult {
    interface Raw {
        additionalParameters: serializers.v2.Parameter.Raw[];
        code: serializers.v2.FunctionImplementationForMultipleLanguages.Raw;
    }
}